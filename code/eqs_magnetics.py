"""
Module with custom functions for running magnetic equivalent sources.
"""
import numpy as np
import verde as vd
import choclo
import numba

# Magnetic constant (henry/meter)
# CM = 1e-7
CM = choclo.constants.VACUUM_MAGNETIC_PERMEABILITY / (4 * np.pi)
TESLA_TO_NANOTESLA = 1e9


def unit_vector(inclination, declination):
    """
    Generate a 3-component unit vector from the direction angles.
    
    Inclination is positive downwards and declination is the angle with
    the North component.
    
    The unit vector has easting, northing, and upward components.
    """
    easting = np.cos(np.radians(-inclination)) * np.sin(np.radians(declination))
    northing = np.cos(np.radians(-inclination)) * np.cos(np.radians(declination))
    upward = np.sin(np.radians(-inclination))
    return np.array([easting, northing, upward])


def dipole_magnetic_field_fast(data_coordinates, dipole_coordinates, dipole_moment):
    """
    Magnetic field of a dipole (full 3-component vector).
    Output is in nanotesla.
    """
    data_shape = data_coordinates[0].shape
    data_coordinates = [np.asarray(c).ravel() for c in data_coordinates]
    dipole_coordinates = [np.asarray(c).ravel() for c in dipole_coordinates]
    dipole_moment = np.asarray(dipole_moment)
    if dipole_moment.ndim == 1:
        dipole_moment = np.array([dipole_moment])
    magnetic_field = [np.zeros(data_coordinates[0].shape) for i in range(3)]
    _dipole_magnetic_field_fast(
        data_coordinates[0], 
        data_coordinates[1], 
        data_coordinates[2], 
        dipole_coordinates[0],
        dipole_coordinates[1],
        dipole_coordinates[2], 
        dipole_moment, 
        magnetic_field[0],
        magnetic_field[1],
        magnetic_field[2],
    )    
    return [TESLA_TO_NANOTESLA * m.reshape(data_shape) for m in magnetic_field]


@numba.jit(nopython=True, parallel=True)
def _dipole_magnetic_field_fast(easting, northing, upward, d_easting, d_northing, d_upward, dipole_moment, bx, by, bz):
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
                magnetic_moment=dipole_moment[j, :],
            )
            bx[i] += field[0]
            by[i] += field[1]
            bz[i] += field[2]
    

def dipole_magnetic_field(data_coordinates, dipole_coordinates, dipole_moment):
    """
    Magnetic field of a dipole (full 3-component vector).
    Output is in nanotesla.
    """
    dipole_coordinates = [np.atleast_1d(c).ravel() for c in dipole_coordinates]
    number_of_dipoles = dipole_coordinates[0].size
    magnetic_field = [np.zeros(data_coordinates[0].shape) for i in range(3)]
    for j in range(number_of_dipoles):
        distance = np.sqrt(
            (dipole_coordinates[0][j] - data_coordinates[0])**2 
            + (dipole_coordinates[1][j] - data_coordinates[1])**2 
            + (dipole_coordinates[2][j] - data_coordinates[2])**2
        )
        # Calculate unit vector r between the source and the data
        distance_unit_vector = [
            (dipole[j] - data) / distance 
            for dipole, data in zip(dipole_coordinates, data_coordinates)
        ]
        m_dot_r = sum(
            m * r 
            for m, r in zip(dipole_moment[j], distance_unit_vector)
        )    
        be, bn, bu = [
            (TESLA_TO_NANOTESLA * CM / distance**3)
            * (3 * m_dot_r * r  - m)
            for m, r in zip(dipole_moment[j], distance_unit_vector)
        ]
        magnetic_field[0] += be
        magnetic_field[1] += bn
        magnetic_field[2] += bu
    return magnetic_field


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


def optimal_source_depth(data_coordinates):
    """
    Estimates optimal depth of sources based on their horizontal spacing.
    """
    spacing = np.median(vd.median_distance(data_coordinates))
    lowerbound = 2.5 * spacing
    upperbound = 6 * spacing
    depth = (lowerbound + upperbound) / 2
    return depth

        
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


def damped_least_squares(data, sensitivity, damping):
    I = np.identity(sensitivity.shape[1]) # needs to = m x m
    system_matrix = sensitivity.T @ sensitivity + I * damping
    system_rhs_vector = sensitivity.T @ data
    coefficients = np.linalg.solve(system_matrix, system_rhs_vector)
    return coefficients


def fit(coordinates, data, eqs_source_coords, damping, eqs_inc, eqs_dec, main_field_direction):
    A = sensitivity_matrix(
        coordinates, 
        eqs_source_coords, 
        unit_vector(eqs_inc, eqs_dec),
        main_field_direction,
    )
    eqs_dipole_moment_amplitude = damped_least_squares(
        data, A, damping=damping,
    )
    return eqs_dipole_moment_amplitude


def deep_eqs_coords(data_coords, eqs_spacing, eqs_depth):
    reducer = vd.BlockReduce(reduction=np.median,
                             spacing=eqs_spacing,
                             center_coordinates=False)
    points, _ = reducer.filter(data_coords, data_coords[0])
    eqs_coords_deep = list(points)
    eqs_coords_deep.append(np.full_like(points[0], eqs_depth))
    return eqs_coords_deep

def deep_dipole_moment(data_coords, data, eqs_inclination, eqs_declination, eqs_dipole_unit, damping, deep_eqs_coords, main_field_direction):
    deep_dipole_moment_amp = fit(
        coordinates=data_coords,
        data=data,
        eqs_source_coords=deep_eqs_coords,
        damping=damping,
        eqs_inc=eqs_inclination,
        eqs_dec=eqs_declination,
        main_field_direction=main_field_direction
    )
    dipole_moment_deep = [
        deep_dipole_moment_amp[j] * eqs_dipole_unit
        for j in range(deep_dipole_moment_amp.size)
    ]
    return dipole_moment_deep


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