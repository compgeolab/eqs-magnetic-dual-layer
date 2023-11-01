"""
Module with custom functions for running magnetic equivalent sources.
"""
import numpy as np
import sklearn.utils
import sklearn.utils.validation
import verde as vd
import verde.base as vdb
import harmonica as hm
import choclo
import numba

# Magnetic constant (henry/meter)
# CM = 1e-7
CM = choclo.constants.VACUUM_MAGNETIC_PERMEABILITY / (4 * np.pi)
TESLA_TO_NANOTESLA = 1e9


def contaminate(data, standard_deviation, random_state=None):
    """
    Add pseudo-random gaussian noise to the data array **in-place**.
    """
    noise = sklearn.utils.check_random_state(random_state).normal(
        0, standard_deviation, size=data.shape,
    )
    data += noise
    return data


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
    # Dampney recommends between 2.5 and 6 x spacing. Take the average.
    depth = 4.25 * spacing
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
        sklearn.utils.validation.check_is_fitted(self, ["dipole_moments_"])
        return np.asarray(dipole_magnetic(coordinates, self.dipole_coordinates_, self.dipole_moments_))

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
        n = len(coordinates[0])
        m = len(dipole_coordinates[0])
        A = np.empty((n, m))
        _jacobian_fast(
            easting=coordinates[0],
            northing=coordinates[1],
            upward=coordinates[2],
            d_easting=dipole_coordinates[0],
            d_northing=dipole_coordinates[1],
            d_upward=dipole_coordinates[2],
            m_easting=dipole_moment_direction[0][0],
            m_northing=dipole_moment_direction[1][0],
            m_upward=dipole_moment_direction[2][0],
            f_easting=field_direction[0][0],
            f_northing=field_direction[1][0],
            f_upward=field_direction[2][0],
            jacobian=A,
        )
        return A


@numba.jit(nopython=True, parallel=True)
def _jacobian_fast(
    easting, northing, upward, d_easting, d_northing, d_upward, m_easting,
    m_northing, m_upward, f_easting, f_northing, f_upward, jacobian,
):
        for i in numba.prange(easting.size):
            for j in range(d_easting.size):
                b_easting, b_northing, b_upward = choclo.dipole.magnetic_field(
                    easting_p=easting[i],
                    northing_p=northing[i],
                    upward_p=upward[i],
                    easting_q=d_easting[j],
                    northing_q=d_northing[j],
                    upward_q=d_upward[j],
                    magnetic_moment_east=m_easting,
                    magnetic_moment_north=m_northing,
                    magnetic_moment_up=m_upward,
                )
                jacobian[i, j] = TESLA_TO_NANOTESLA * (
                    b_easting * f_easting
                    + b_northing * f_northing
                    + b_upward * f_upward
                )



class EquivalentSourcesMagneticGB(EquivalentSourcesMagnetic):

    def __init__(
        self, damping=None, depth=None, block_size=None,
        dipole_inclination=90, dipole_declination=0, dipole_coordinates=None,
        window_size=None, repeat=1, random_state=None,
    ):
        super().__init__(
            damping, depth, block_size, dipole_inclination, dipole_declination,
            dipole_coordinates,
        )
        self.window_size = window_size
        self.repeat = repeat
        self.random_state = random_state
       
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
        if self.window_size is None:
            # Keep the data per window around 10k.
            # A better way would be to figure out the RAM available and choose
            # based on that.
            area = (self.region_[1] - self.region_[0]) * (self.region_[3] - self.region_[2])
            ndata = data.size
            points_per_m2 = ndata / area
            window_area = 5e3 / points_per_m2
            self.window_size_ = np.sqrt(window_area)
        else:
            self.window_size_ = self.window_size

        _, dipole_windows = vd.rolling_window(
            self.dipole_coordinates_,
            region=self.region_,
            size=self.window_size_,
            spacing=self.window_size_ / 2,
        )
        _, data_windows = vd.rolling_window(
            coordinates,
            region=self.region_,
            size=self.window_size_,
            spacing=self.window_size_ / 2
        )
        dipole_windows = [i[0] for i in dipole_windows.ravel()]
        data_windows = [i[0] for i in data_windows.ravel()]
        # remove empty windows
        dipole_windows_nonempty = []
        data_windows_nonempty = []
        for dipole_window_, data_window_ in zip(dipole_windows, data_windows):
            if dipole_window_.size > 0 and data_window_.size > 0:
                dipole_windows_nonempty.append(dipole_window_)
                data_windows_nonempty.append(data_window_)
    
        residuals = data.copy()
        moment_amplitude = np.zeros_like(self.dipole_coordinates_[0])
        window_indices = list(range(len(data_windows_nonempty)))
        for iteration in range(self.repeat):
            sklearn.utils.check_random_state(self.random_state).shuffle(window_indices)
            for window in window_indices:
                dipole_window, data_window = dipole_windows_nonempty[window], data_windows_nonempty[window]
                coords_chunk = tuple(c[data_window] for c in coordinates)
                dipole_chunk = tuple(c[dipole_window] for c in self.dipole_coordinates_)
                if weights is not None:
                    weights_chunk = weights[data_window]
                else:
                    weights_chunk = None
                jacobian = self.jacobian(
                    coords_chunk, dipole_chunk, dipole_moment_direction, field_direction,
                )
                moment_amplitude_chunk = vdb.least_squares(
                    jacobian, residuals[data_window], weights_chunk, self.damping,
                )
                dipole_moment_chunk = angles_to_vector(
                    self.dipole_inclination, self.dipole_declination, moment_amplitude_chunk,
                )
                predicted = total_field_anomaly(
                    dipole_magnetic(coordinates, dipole_chunk, dipole_moment_chunk),
                    field_direction,
                )
                moment_amplitude[dipole_window] += moment_amplitude_chunk
                residuals -= predicted
        self.dipole_moments_ = angles_to_vector(
            self.dipole_inclination, self.dipole_declination, moment_amplitude,
        )
        return self
