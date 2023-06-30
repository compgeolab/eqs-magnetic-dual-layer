"""
Module with custom functions for running magnetic equivalent sources.
"""
import numpy as np
from sklearn.utils.validation import check_is_fitted
import verde as vd
import verde.base as vdb
import harmonica as hm
import choclo
import numba

# Magnetic constant (henry/meter)
# CM = 1e-7
CM = choclo.constants.VACUUM_MAGNETIC_PERMEABILITY / (4 * np.pi)
TESLA_TO_NANOTESLA = 1e9


def angles_to_vector(inclination, declination, amplitude):
    """
    Generate a 3-component vector from inclination, declination, and amplitude

    Inclination is positive downwards and declination is the angle with the y
    component. The vector has x, y, and z (upward) Cartesian components.

    Parameters
    ----------
    inclination : float or array
        The inclination values in degrees.
    declination : float or array
        The declination values in degrees.
    amplitude : float or array
        The vector amplitude values.

    Returns
    -------
    vector : 1D or 2D array
        The calculated x, y, z vector components. 1D if it's a single vector.
        If N vectors are calculated, the "vector" will have shape (N, 3) with
        each vector in a row of the array.
    """
    inclination = np.radians(np.atleast_1d(inclination))
    declination = np.radians(np.atleast_1d(declination))
    amplitude = np.atleast_1d(amplitude)
    sin_inc = np.sin(-inclination)
    cos_inc = np.cos(-inclination)
    sin_dec = np.sin(declination)
    cos_dec = np.cos(declination)
    x = cos_inc * sin_dec * amplitude
    y = cos_inc * cos_dec * amplitude
    z = sin_inc * amplitude
    return np.array([x, y, z])


def dipole_magnetic(coordinates, dipoles, magnetic_moments):
    """
    Magnetic field of a dipole (full 3-component vector).
    Output is in nanotesla.
    """
    data_shape = coordinates[0].shape
    coordinates = [np.asarray(c).ravel() for c in coordinates]
    dipoles = [np.asarray(c).ravel() for c in dipoles]
    magnetic_moments = [np.asarray(c).ravel() for c in magnetic_moments]
    magnetic_field = [np.zeros(coordinates[0].shape) for i in range(3)]
    _dipole_magnetic_field_fast(
        coordinates[0],
        coordinates[1],
        coordinates[2],
        dipoles[0],
        dipoles[1],
        dipoles[2],
        magnetic_moments[0],
        magnetic_moments[1],
        magnetic_moments[2],
        magnetic_field[0],
        magnetic_field[1],
        magnetic_field[2],
    )
    return [TESLA_TO_NANOTESLA * m.reshape(data_shape) for m in magnetic_field]


@numba.jit(nopython=True, parallel=True)
def _dipole_magnetic_field_fast(
    easting, northing, upward, d_easting, d_northing, d_upward, m_easting,
    m_northing, m_upward, b_easting, b_northing, b_upward,
):
    """
    This is the bit that runs the fast for-loops
    """
    for i in numba.prange(easting.size):
        for j in range(d_easting.size):
            field = choclo.dipole.magnetic_field(
                easting_p=easting[i],
                northing_p=northing[i],
                upward_p=upward[i],
                easting_q=d_easting[j],
                northing_q=d_northing[j],
                upward_q=d_upward[j],
                magnetic_moment_east=m_easting[j],
                magnetic_moment_north=m_northing[j],
                magnetic_moment_up=m_upward[j],
            )
            b_easting[i] += field[0]
            b_northing[i] += field[1]
            b_upward[i] += field[2]


def total_field_anomaly(source_magnetic_field, main_field_direction):
    """
    Total-field anomaly from a source field and main field direction.
    Output in nanotesla.
    """
    b_east, b_north, b_up = source_magnetic_field
    f_east, f_north, f_up = main_field_direction
    result = b_east * f_east + b_north * f_north + b_up * f_up
    return result


def magnetic_field_norm(magnetic_field):
    """
    Calculate the point-wise norm of the magnetic field.
    """
    b_east, b_north, b_up = magnetic_field
    norm = np.sqrt(b_east**2 + b_north**2 + b_up**2)
    return norm


def recommended_source_depth(coordinates):
    """
    Estimates an approximate depth of sources based on their horizontal spacing
    From Dampney (1969).
    """
    spacing = np.mean(vd.median_distance(coordinates))
    lowerbound = 2.5 * spacing
    upperbound = 6 * spacing
    depth = (lowerbound + upperbound) / 2
    return depth


class EquivalentSourcesMagnetic():

    def __init__(
        self, damping=None, depth=None, block_size=None,
        dipole_inclination=90, dipole_declination=0, dipole_coordinates=None,
    ):
        self.damping = damping
        self.depth = depth
        self.block_size = block_size
        self.dipole_coordinates = dipole_coordinates
        self.dipole_inclination = dipole_inclination
        self.dipole_declination = dipole_declination

    def fit(self, coordinates, data, field_direction, weights=None):
        """
        """
        coordinates, data, weights = vdb.check_fit_input(coordinates, data, weights)
        # Capture the data region to use as a default when gridding.
        self.region_ = vd.get_region(coordinates[:2])
        coordinates = vdb.n_1d_arrays(coordinates, 3)
        self.dipole_coordinates_ = self._build_points(coordinates)
        dipole_moment_direction = angles_to_vector(
            self.dipole_inclination, self.dipole_declination, 1,
        )
        jacobian = self.jacobian(
            coordinates, self.dipole_coordinates_, dipole_moment_direction, field_direction,
        )
        moment_amplitude = vdb.least_squares(jacobian, data, weights, self.damping)
        self.dipole_moments_ = angles_to_vector(
            self.dipole_inclination, self.dipole_declination, moment_amplitude,
        )
        return self

    def predict(self, coordinates):
        """
        """
        # We know the gridder has been fitted if it has the estimated parameters
        check_is_fitted(self, ["dipole_moments_"])
        return dipole_magnetic(coordinates, self.dipole_coordinates_, self.dipole_moments_)

    def _build_points(self, coordinates):
        """
        """
        if self.depth is None:
            depth = recommended_source_depth(coordinates)
        else:
            depth = self.depth
        if self.block_size is not None:
            reducer = vd.BlockReduce(
                spacing=self.block_size, reduction=np.median, drop_coords=False
            )
            # Must pass a dummy data array to BlockReduce.filter(), we choose
            # one of the coordinate arrays. We will ignore the returned reduced
            # dummy array.
            coordinates, _ = reducer.filter(coordinates, coordinates[0])
        points = [
            coordinates[0],
            coordinates[1],
            coordinates[2] - depth,
        ]
        return points

    def jacobian(
        self, coordinates, dipole_coordinates, dipole_moment_direction, field_direction,
    ):
        """
        """
        dipole_coordinates = [c.ravel() for c in dipole_coordinates]
        n = len(coordinates[0])
        m = len(dipole_coordinates[0])
        A = np.empty((n, m))
        for j in range(m):
            east = dipole_coordinates[0][j]
            north = dipole_coordinates[1][j]
            up = dipole_coordinates[2][j]
            magnetic_field = dipole_magnetic(
                coordinates, ([east], [north], [up]), dipole_moment_direction,
            )
            A[:, j] = total_field_anomaly(magnetic_field, field_direction)
        return A




def sensitivity_matrix(
    data_coords, source_coords, unit_dipole_moment, main_field_direction,
):
    """
    Calculate the A matrix using the total field anomaly.
    """
    source_coords = [c.ravel() for c in source_coords]
    n = len(data_coords[0])
    m = len(source_coords[0])
    A = np.empty((n, m))
    for j in range(m):
        east = source_coords[0][j]
        north = source_coords[1][j]
        up = source_coords[2][j]
        magnetic_field = dipole_magnetic_field_fast(
            data_coords, ([east], [north], [up]), [unit_dipole_moment],
        )
        A[:, j] = total_field_anomaly(magnetic_field, main_field_direction)
    return A


def shallow_dipole_moment_amp(data_coords, eqs_coords_shallow, window_size, damping, residuals, eqs_inclination, eqs_declination, eqs_dipole_unit, main_field_direction):
    _, source_indices = vd.rolling_window(
        eqs_coords_shallow,
        size=window_size,
        spacing=window_size / 2,
    )
    _, data_indices = vd.rolling_window(
        data_coords,
        size=window_size,
        spacing=window_size / 2
    )
    source_indices = [i[0] for i in source_indices.ravel()]
    data_indices = [i[0] for i in data_indices.ravel()]
    rmses = []
    residuals_shallow = residuals.copy()
    dipole_moment_amp_shallow = np.zeros_like(eqs_coords_shallow[0])
    window_indices = list(range(len(data_indices)))
    np.random.shuffle(window_indices)
    for i in window_indices:
        data_coord = tuple(c[data_indices[i]] for c in data_coords)
        source_coord = tuple(c[source_indices[i]] for c in eqs_coords_shallow)
        eqs_dipole_moment_amp_shallow = fit(
            coordinates=data_coord,
            data=residuals_shallow[data_indices[i]],
            eqs_source_coords=source_coord,
            damping=damping,
            eqs_inc=eqs_inclination,
            eqs_dec=eqs_declination,
            main_field_direction=main_field_direction,
        )
        dipole_moment_amp_shallow[source_indices[i]] += eqs_dipole_moment_amp_shallow
        dipole_moment_shallow = [
            eqs_dipole_moment_amp_shallow[j] * eqs_dipole_unit
            for j in range(eqs_dipole_moment_amp_shallow.size)
        ]
        predicted_tfa_shallow = total_field_anomaly(
            dipole_magnetic_field_fast(
                data_coords,
                source_coord,
                dipole_moment_shallow,
            ),
            main_field_direction,
        )
        residuals_shallow -= predicted_tfa_shallow

    return dipole_moment_amp_shallow, residuals_shallow
