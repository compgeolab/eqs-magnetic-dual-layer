"""
Module with custom functions for running synthetic datasets.
"""
import numpy as np
import verde as vd
import eqs_magnetics as eqs
import harmonica as hm

def generate_profile(first, last, size, height, magnitude, direction):
    coords = vd.profile_coordinates(first, last, size=size, extra_coords=height)[0]
    moments = np.array(hm.magnetic_angles_to_vec(np.full(size, magnitude), direction[0], direction[1]))
    return coords, moments

def generate_source(source, height, magnitude, profiles, grid=None):
    coordinates = []
    dipole_moments = []
    if grid:
        grid_shape, grid_magnitude, region = grid
        grid_size = grid_shape[0] * grid_shape[1]
        coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates(region, shape=grid_shape, extra_coords=height)])
        dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(grid_size, grid_magnitude), source[0], source[1])))
    
    for first, last, size in profiles:
        coords, moments = generate_profile(first, last, size, height, magnitude, source)
        coordinates.append(coords)
        dipole_moments.append(moments)
    return coordinates, dipole_moments

def generate_dipoles(coords, magnitude, direction, coordinates, dipole_moments):
    for coord in coords:
        coordinates.append(coord)
        _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(magnitude, direction[0], direction[1])
        dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))

def icegrav_synthetic(source1, source2, source3, source4, dyke1, dyke2, dipoles, regional_dipole, regional):
    """
    Synthetic dataset associated with the ICEGRAV coordinates.
    Provide source directions specifed as [inclination, declination]. E.g. source1=[-60,60], where inclination=-60 and declination=60.
    """
    sources = [
        (source1, -6e3, 2e10, [
            ((1.914e6, 3.036e6), (1.946e6, 3.036e6), 14),
            ((1.920e6, 3.037e6), (1.940e6, 3.037e6), 12),
            ((1.926e6, 3.038e6), (1.934e6, 3.038e6), 5),
            ((1.908e6, 3.017e6), (1.908e6, 3.033e6), 14),
            ((1.914e6, 3.014e6), (1.946e6, 3.014e6), 14),
            ((1.920e6, 3.013e6), (1.940e6, 3.013e6), 12),
            ((1.926e6, 3.012e6), (1.934e6, 3.012e6), 5),
            ((1.952e6, 3.017e6), (1.952e6, 3.033e6), 14),
            ((1.954e6, 3.020e6), (1.954e6, 3.029e6), 10),
        ], ((20, 20), 1e10, [1.91e6, 1.95e6, 3.015e6, 3.035e6])),
        (source2, -800, 3e9, [
            ((1.960e6, 2.974e6), (1.986e6, 3.000e6), 30),
            ((1.960e6, 2.972e6), (1.988e6, 3.000e6), 30),
            ((1.960e6, 2.970e6), (1.990e6, 3.000e6), 30),
            ((1.960e6, 2.968e6), (1.990e6, 2.998e6), 30),
            ((1.960e6, 2.966e6), (1.990e6, 2.996e6), 30),
            ((1.946e6, 2.950e6), (1.990e6, 2.994e6), 40),
            ((1.946e6, 2.948e6), (1.990e6, 2.992e6), 40),
            ((1.946e6, 2.946e6), (1.990e6, 2.990e6), 40),
            ((1.946e6, 2.944e6), (1.990e6, 2.988e6), 40),
            ((1.946e6, 2.942e6), (1.990e6, 2.986e6), 40),
            ((1.946e6, 2.940e6), (1.990e6, 2.984e6), 40),
            ((1.946e6, 2.948e6), (1.990e6, 2.982e6), 40),
            ((1.947e6, 2.946e6), (1.990e6, 2.980e6), 40),
        ]),
        (source3, -900, 5e9, [
            ((2.21e6, 2.8185e6), (2.23e6, 2.823e6), 10),
            ((2.208e6, 2.817e6), (2.234e6, 2.823e6), 15),
            ((2.206e6, 2.8155e6), (2.24e6, 2.8235e6), 20),
            ((2.202e6, 2.8135e6), (2.246e6, 2.824e6), 20),
            ((2.20e6, 2.812e6), (2.25e6, 2.824e6), 20),
            ((2.20e6, 2.811e6), (2.254e6, 2.824e6), 20),
            ((2.20e6, 2.81e6), (2.257e6, 2.824e6), 25),
            ((2.20e6, 2.809e6), (2.259e6, 2.8235e6), 20),
            ((2.202e6, 2.8086e6), (2.26e6, 2.8225e6), 20),
            ((2.205e6, 2.8086e6), (2.26e6, 2.8215e6), 20),
            ((2.209e6, 2.8087e6), (2.259e6, 2.8205e6), 20),
            ((2.215e6, 2.809e6), (2.257e6, 2.819e6), 20),
        ]),
        (source4, -8e3, 1e10, [
            ((2.236e6, 2.736e6), (2.266e6, 2.736e6), 14),
            ((2.220e6, 2.737e6), (2.260e6, 2.737e6), 12),
            ((2.226e6, 2.738e6), (2.254e6, 2.738e6), 5),
            ((2.238e6, 2.734e6), (2.238e6, 2.713e6), 14),
            ((2.240e6, 2.711e6), (2.266e6, 2.711e6), 14),
            ((2.244e6, 2.713e6), (2.260e6, 2.713e6), 12),
            ((2.246e6, 2.715e6), (2.264e6, 2.715e6), 5),
        ], ((20, 20), 9e9, [2.24e6, 2.265e6, 2.715e6, 2.735e6])),
        (dyke1, -1e3, 1e9, [
            ((2.18e6,2.9e6),(2.205e6,3.0e6), 500),
            ((2.185e6,2.9e6),(2.21e6,3.0e6), 500),
        ]),
        (dyke2, -5e3, 2e9, [
            ((2.16e6, 2.76e6), (2.26e6, 2.98e6), 1000),
            ((2.165e6, 2.76e6), (2.261e6, 2.98e6), 1000),
            ((2.17e6, 2.76e6), (2.262e6, 2.98e6), 1000),
            ((2.185e6, 2.78e6), (2.263e6, 2.98e6), 900),
            ((2.19e6, 2.78e6), (2.264e6, 2.98e6), 800),
            ((2.195e6, 2.78e6), (2.265e6, 2.98e6), 900),
        ]),
    ]
    coordinates, dipole_moments = [], []
    for source in sources:
        coords, moments = generate_source(*source)
        coordinates.extend(coords)
        dipole_moments.extend(moments)
    
    small_dipole_height = -500
    small_dipole_moment = 5e10
    small_dipole_coords = [
        [[1.95e6], [2.785e6], [small_dipole_height]],
        [[2.1e6], [3.011e6], [small_dipole_height]],
        [[2.11e6], [2.955e6], [small_dipole_height]],
        [[2.15e6], [2.75e6], [small_dipole_height]],
    ]
    generate_dipoles(small_dipole_coords, small_dipole_moment, dipoles, coordinates, dipole_moments)
    
    regional_dipole_height = -70e3
    regional_dipole_moment = 2e13
    regional_dipole_coords = [
        [[2035e3], [2925e3], [regional_dipole_height]],
        [[2050e3], [2925e3], [regional_dipole_height]],
        [[2020e3], [2910e3], [regional_dipole_height]],
        [[2035e3], [2910e3], [regional_dipole_height]],
        [[2050e3], [2910e3], [regional_dipole_height]],
        [[2075e3], [2910e3], [regional_dipole_height]],
        [[2020e3], [2895e3], [regional_dipole_height]],
        [[2035e3], [2895e3], [regional_dipole_height]],
        [[2050e3], [2895e3], [regional_dipole_height]],
        [[2075e3], [2915e3], [regional_dipole_height]],
        [[2005e3], [2880e3], [regional_dipole_height]],
        [[2020e3], [2880e3], [regional_dipole_height]],
        [[2035e3], [2880e3], [regional_dipole_height]],
        [[2050e3], [2880e3], [regional_dipole_height]],
        [[2075e3], [2880e3], [regional_dipole_height]],
        [[2090e3], [2880e3], [regional_dipole_height]],
        [[2100e3], [2880e3], [regional_dipole_height]],
        [[2005e3], [2865e3], [regional_dipole_height]],
        [[2020e3], [2865e3], [regional_dipole_height]],
        [[2035e3], [2865e3], [regional_dipole_height]],
        [[2050e3], [2865e3], [regional_dipole_height]],
        [[2075e3], [2865e3], [regional_dipole_height]],
        [[2090e3], [2865e3], [regional_dipole_height]],
        [[2100e3], [2865e3], [regional_dipole_height]],
        [[2020e3], [2850e3], [regional_dipole_height]],
        [[2035e3], [2850e3], [regional_dipole_height]],
        [[2050e3], [2850e3], [regional_dipole_height]],
        [[2075e3], [2850e3], [regional_dipole_height]],
        [[2020e3], [2850e3], [regional_dipole_height]],
        [[2035e3], [2850e3], [regional_dipole_height]],
        [[2050e3], [2835e3], [regional_dipole_height]],
        [[2065e3], [2835e3], [regional_dipole_height]],
        [[2035e3], [2820e3], [regional_dipole_height]],
        [[2050e3], [2820e3], [regional_dipole_height]],   
    ]
    generate_dipoles(regional_dipole_coords, regional_dipole_moment, regional_dipole, coordinates, dipole_moments)
    
    # Regional field
    region = [1.85e6,2.35e6,2.54e6,3.1e6]
    easting, northing = vd.grid_coordinates(region, shape=(30,30))
    upward = vd.synthetic.CheckerBoard(region=region, amplitude=15e3, w_east=0.25e6, w_north=0.25e6).predict((easting, northing)) + -60e3
    regional_coords = (easting, northing, upward)
    for i, c in enumerate(regional_coords):
        eqs.contaminate(c, standard_deviation=5, random_state=i)
    coordinates.append([np.asarray(c).ravel() for c in regional_coords])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(900,5e12), regional[0], regional[1])))
    
    coordinates = np.concatenate(coordinates, axis=1)
    dipole_moments = np.concatenate(dipole_moments, axis=1)
    return coordinates, dipole_moments

def truncated_regional_synthetic(source1, source2, source3, source4, dyke1, dyke2, dipoles, regional):
    """
    Same as the icegrav_synthetic but without the regional dipole.
    Synthetic dataset associated with the ICEGRAV coordinates.
    Provide source directions specifed as [inclination, declination]. E.g. source1=[-60,60], where inclination=-60 and declination=60.
    """
    sources = [
        (source1, -6e3, 2e10, [
            ((1.914e6, 3.036e6), (1.946e6, 3.036e6), 14),
            ((1.920e6, 3.037e6), (1.940e6, 3.037e6), 12),
            ((1.926e6, 3.038e6), (1.934e6, 3.038e6), 5),
            ((1.908e6, 3.017e6), (1.908e6, 3.033e6), 14),
            ((1.914e6, 3.014e6), (1.946e6, 3.014e6), 14),
            ((1.920e6, 3.013e6), (1.940e6, 3.013e6), 12),
            ((1.926e6, 3.012e6), (1.934e6, 3.012e6), 5),
            ((1.952e6, 3.017e6), (1.952e6, 3.033e6), 14),
            ((1.954e6, 3.020e6), (1.954e6, 3.029e6), 10),
        ], ((20, 20), 1e10, [1.91e6, 1.95e6, 3.015e6, 3.035e6])),
        (source2, -800, 3e9, [
            ((1.960e6, 2.974e6), (1.986e6, 3.000e6), 30),
            ((1.960e6, 2.972e6), (1.988e6, 3.000e6), 30),
            ((1.960e6, 2.970e6), (1.990e6, 3.000e6), 30),
            ((1.960e6, 2.968e6), (1.990e6, 2.998e6), 30),
            ((1.960e6, 2.966e6), (1.990e6, 2.996e6), 30),
            ((1.946e6, 2.950e6), (1.990e6, 2.994e6), 40),
            ((1.946e6, 2.948e6), (1.990e6, 2.992e6), 40),
            ((1.946e6, 2.946e6), (1.990e6, 2.990e6), 40),
            ((1.946e6, 2.944e6), (1.990e6, 2.988e6), 40),
            ((1.946e6, 2.942e6), (1.990e6, 2.986e6), 40),
            ((1.946e6, 2.940e6), (1.990e6, 2.984e6), 40),
            ((1.946e6, 2.948e6), (1.990e6, 2.982e6), 40),
            ((1.947e6, 2.946e6), (1.990e6, 2.980e6), 40),
        ]),
        (source3, -900, 5e9, [
            ((2.21e6, 2.8185e6), (2.23e6, 2.823e6), 10),
            ((2.208e6, 2.817e6), (2.234e6, 2.823e6), 15),
            ((2.206e6, 2.8155e6), (2.24e6, 2.8235e6), 20),
            ((2.202e6, 2.8135e6), (2.246e6, 2.824e6), 20),
            ((2.20e6, 2.812e6), (2.25e6, 2.824e6), 20),
            ((2.20e6, 2.811e6), (2.254e6, 2.824e6), 20),
            ((2.20e6, 2.81e6), (2.257e6, 2.824e6), 25),
            ((2.20e6, 2.809e6), (2.259e6, 2.8235e6), 20),
            ((2.202e6, 2.8086e6), (2.26e6, 2.8225e6), 20),
            ((2.205e6, 2.8086e6), (2.26e6, 2.8215e6), 20),
            ((2.209e6, 2.8087e6), (2.259e6, 2.8205e6), 20),
            ((2.215e6, 2.809e6), (2.257e6, 2.819e6), 20),
        ]),
        (source4, -8e3, 1e10, [
            ((2.236e6, 2.736e6), (2.266e6, 2.736e6), 14),
            ((2.220e6, 2.737e6), (2.260e6, 2.737e6), 12),
            ((2.226e6, 2.738e6), (2.254e6, 2.738e6), 5),
            ((2.238e6, 2.734e6), (2.238e6, 2.713e6), 14),
            ((2.240e6, 2.711e6), (2.266e6, 2.711e6), 14),
            ((2.244e6, 2.713e6), (2.260e6, 2.713e6), 12),
            ((2.246e6, 2.715e6), (2.264e6, 2.715e6), 5),
        ], ((20, 20), 9e9, [2.24e6, 2.265e6, 2.715e6, 2.735e6])),
        (dyke1, -1e3, 1e9, [
            ((2.18e6,2.9e6),(2.205e6,3.0e6), 500),
            ((2.185e6,2.9e6),(2.21e6,3.0e6), 500),
        ]),
        (dyke2, -5e3, 2e9, [
            ((2.16e6, 2.76e6), (2.26e6, 2.98e6), 1000),
            ((2.165e6, 2.76e6), (2.261e6, 2.98e6), 1000),
            ((2.17e6, 2.76e6), (2.262e6, 2.98e6), 1000),
            ((2.185e6, 2.78e6), (2.263e6, 2.98e6), 900),
            ((2.19e6, 2.78e6), (2.264e6, 2.98e6), 800),
            ((2.195e6, 2.78e6), (2.265e6, 2.98e6), 900),
        ]),
    ]
    coordinates, dipole_moments = [], []
    for source in sources:
        coords, moments = generate_source(*source)
        coordinates.extend(coords)
        dipole_moments.extend(moments)
    
    small_dipole_height = -500
    small_dipole_moment = 5e10
    small_dipole_coords = [
        [[1.95e6], [2.785e6], [small_dipole_height]],
        [[2.1e6], [3.011e6], [small_dipole_height]],
        [[2.11e6], [2.955e6], [small_dipole_height]],
        [[2.15e6], [2.75e6], [small_dipole_height]],
    ]
    generate_dipoles(small_dipole_coords, small_dipole_moment, dipoles, coordinates, dipole_moments)
    
    # Regional field
    region = [1.85e6,2.35e6,2.54e6,3.1e6]
    easting, northing = vd.grid_coordinates(region, shape=(30,30))
    upward = vd.synthetic.CheckerBoard(region=region, amplitude=15e3, w_east=0.25e6, w_north=0.25e6).predict((easting, northing)) + -60e3
    regional_coords = (easting, northing, upward)
    for i, c in enumerate(regional_coords):
        eqs.contaminate(c, standard_deviation=5, random_state=i)
    coordinates.append([np.asarray(c).ravel() for c in regional_coords])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(900,5e12), regional[0], regional[1])))
    
    coordinates = np.concatenate(coordinates, axis=1)
    dipole_moments = np.concatenate(dipole_moments, axis=1)
    return coordinates, dipole_moments


def simple_synthetic(dyke1, dyke2, point1, point2, point3, point4, regional ):
    """
    Simple synthetic dataset associated with the Victoria Land coordinates.
    Provide source directions specifed as [inclination, declination]. E.g. dyke1=[70,60], where inclination=70 and declination=60.
    """
    dipole_moments = []
    coordinates = []
    dyke_moment_magnitude = 10e7
    # dyke NE-SW
    coordinates.append(vd.profile_coordinates((-20e3, -5e3), (20e3, 12e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dyke1[0], dyke1[1], np.full(1000, dyke_moment_magnitude)))
    # dyke NW-SE
    coordinates.append(vd.profile_coordinates((20e3, -10e3), (-20e3, 25e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dyke2[0], dyke2[1], np.full(1000, dyke_moment_magnitude)))
    # dyke small
    coordinates.append(vd.profile_coordinates((20e3, -4e3), (4e3, 3e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dyke2[0], dyke2[1], np.full(1000, dyke_moment_magnitude)))
    # dyke very small
    coordinates.append(vd.profile_coordinates((3e3, 3.5e3), (-0.5e3, 5.5e3), size=100, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dyke2[0], dyke2[1], np.full(100, dyke_moment_magnitude)))
    # point source top left
    coordinates.append([[-7500], [7000], [-350]])
    dipole_moments.append(eqs.angles_to_vector(point1[0], point1[1], 6e9))
    # point source centre
    coordinates.append([[0], [-100], [-1e3]])
    dipole_moments.append(eqs.angles_to_vector(point2[0], point2[1], 6e9))
    # point source bottom left
    coordinates.append([[-8000], [-6000], [-800]])
    dipole_moments.append(eqs.angles_to_vector(point3[0], point3[1], 8e9))
    # point source bottom right
    coordinates.append([[7500], [-7500], [-500]])
    dipole_moments.append(eqs.angles_to_vector(point4[0], point4[1], 6e10))    
    # regional
    coordinates.append([[2e3, -5e3], [-9e3, 5e3], [-8e3, -8e3]])
    dipole_moments.append(eqs.angles_to_vector(regional[0], regional[1], np.full(2, 1e13)))
    

    coordinates = np.concatenate(coordinates, axis=1)
    dipole_moments = np.concatenate(dipole_moments, axis=1)
    return coordinates, dipole_moments

def complicated_synthetic(largest_anomaly, grid_anomaly, scatter_anomaly, north_anomaly, south_anomaly, regional):
    """
    Complicated synthetic dataset associated with the Victoria Land coordinates.
    Provide source directions specifed as [inclination, declination]. E.g. dyke1=[70,60], where inclination=70 and declination=60.
    """
    dipole_moments = []
    coordinates = []
    # Largest source
    # Part 1
    coordinates.append(vd.profile_coordinates((260e3,-8.245e6),(310e3,-8.265e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((260e3,-8.25e6),(310e3,-8.27e6), size=2000, extra_coords=-23)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((260e3,-8.255e6),(310e3,-8.275e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((260e3,-8.26e6),(310e3,-8.28e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((260e3,-8.265e6),(310e3,-8.285e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((260e3,-8.27e6),(310e3,-8.29e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((260e3,-8.275e6),(310e3,-8.295e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((270e3,-8.26e6),(310e3,-8.275e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((275e3,-8.26e6),(310e3,-8.28e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((280e3,-8.27e6),(310e3,-8.285e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((280e3,-8.29e6),(325e3,-8.3e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    # Part 2
    coordinates.append(vd.profile_coordinates((285e3,-8.29e6),(380e3,-8.320e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    coordinates.append(vd.profile_coordinates((285e3,-8.295e6),(380e3,-8.325e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    # Part 3
    coordinates.append(vd.profile_coordinates((310e3,-8.31e6),(380e3,-8.33e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    coordinates.append(vd.profile_coordinates((310e3,-8.315e6),(380e3,-8.335e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))   
    coordinates.append(vd.profile_coordinates((300e3,-8.315e6),(380e3,-8.34e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    coordinates.append(vd.profile_coordinates((290e3,-8.32e6),(395e3,-8.345e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    coordinates.append(vd.profile_coordinates((290e3,-8.325e6),(400e3,-8.35e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    coordinates.append(vd.profile_coordinates((290e3,-8.33e6),(395e3,-8.355e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    # Part 4
    coordinates.append(vd.profile_coordinates((345e3,-8.35e6),(395e3,-8.36e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    coordinates.append(vd.profile_coordinates((345e3,-8.355e6),(395e3,-8.365e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    coordinates.append(vd.profile_coordinates((345e3,-8.36e6),(395e3,-8.37e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    coordinates.append(vd.profile_coordinates((340e3,-8.36e6),(400e3,-8.375e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    coordinates.append(vd.profile_coordinates((345e3,-8.365e6),(400e3,-8.38e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    # Part 5
    coordinates.append(vd.profile_coordinates((360e3,-8.37e6),(400e3,-8.385e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((365e3,-8.38e6),(400e3,-8.39e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((370e3,-8.385e6),(405e3,-8.395e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((375e3,-8.39e6),(405e3,-8.40e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((375e3,-8.395e6),(410e3,-8.405e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    # Part 6
    coordinates.append(vd.profile_coordinates((370e3,-8.40e6),(410e3,-8.41e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((370e3,-8.405e6),(415e3,-8.415e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((370e3,-8.41e6),(415e3,-8.42e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((370e3,-8.415e6),(420e3,-8.425e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    # Part 7
    coordinates.append(vd.profile_coordinates((390e3,-8.42e6),(420e3,-8.43e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(85, 75, np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((395e3,-8.425e6),(425e3,-8.435e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((395e3,-8.43e6),(425e3,-8.44e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    coordinates.append(vd.profile_coordinates((395e3,-8.435e6),(430e3,-8.445e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 1e8)))
    # Part 8
    coordinates.append(vd.profile_coordinates((400e3,-8.44e6),(440e3,-8.45e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    coordinates.append(vd.profile_coordinates((405e3,-8.445e6),(435e3,-8.455e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    coordinates.append(vd.profile_coordinates((415e3,-8.45e6),(430e3,-8.46e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    coordinates.append(vd.profile_coordinates((418e3,-8.455e6),(425e3,-8.465e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    coordinates.append(vd.profile_coordinates((419e3,-8.46e6),(422e3,-8.47e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    coordinates.append(vd.profile_coordinates((420e3,-8.46e6),(422e3,-8.47e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    coordinates.append(vd.profile_coordinates((420e3,-8.465e6),(420e3,-8.475e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))

    # North Anomalies
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([340e3,390e3,-8.26e6,-8.20e6,], shape=(100,100), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(north_anomaly[0], north_anomaly[1], np.full(10000, 5e8)))
    coordinates.append(vd.scatter_points([250e3, 430e3, -8.28e6, -8.20e6,], size=1000, random_state=0, extra_coords=-1e3))
    dipole_moments.append(eqs.angles_to_vector(north_anomaly[0]-10, north_anomaly[1]-10, np.full(1000, 1e10)))
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([420e3,430e3,-8.315e6,-8.30e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(north_anomaly[0], north_anomaly[1], np.full(2500, 9e8)))

    # West scatter anomalies
    coordinates.append(vd.scatter_points([250e3, 290e3, -8.34e6, -8.30e6,], size=200, random_state=10,extra_coords=-100))
    dipole_moments.append(eqs.angles_to_vector(scatter_anomaly[0]+10, scatter_anomaly[1]+15, np.full(200, 5e9)))

    # Grid anomaly 1
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([248e3,270e3,-8.38e6,-8.36e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(grid_anomaly[0], grid_anomaly[1], np.full(2500, 9e8)))
    # Grid anomaly 2
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([290e3,310e3,-8.38e6,-8.36e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(grid_anomaly[0], grid_anomaly[1], np.full(2500, 9e8)))
    # Grid anomaly 3
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([330e3,350e3,-8.40e6,-8.38e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(grid_anomaly[0], grid_anomaly[1], np.full(2500, 9e8)))

    # Middle scatter anomaly
    coordinates.append(vd.scatter_points([240e3, 260e3, -8.42e6, -8.38e6,], size=250, random_state=1,extra_coords=-100))
    dipole_moments.append(eqs.angles_to_vector(scatter_anomaly[0], scatter_anomaly[1], np.full(250, 3e9)))
    coordinates.append(vd.scatter_points([310e3, 400e3, -8.46e6, -8.41e6,], size=1000, random_state=2,extra_coords=-100))
    dipole_moments.append(eqs.angles_to_vector(scatter_anomaly[0], scatter_anomaly[1], np.full(1000, 5e9)))

    # South-West anomalies
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([270e3,300e3,-8.47e6,-8.45e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0], south_anomaly[1], np.full(2500, 2e9)))
    coordinates.append(vd.profile_coordinates((260e3,-8.54e6),(300e3,-8.48e6), size=1000, extra_coords=-6e3)[0])
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0]+15, south_anomaly[1]+5, np.full(1000, 5e9)))
    coordinates.append(vd.scatter_points([250e3, 275e3, -8.50e6, -8.485e6,], size=750, random_state=1,extra_coords=-1e3))
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0]-15, south_anomaly[1]-10, np.full(750, 1e9)))
    # South-East Anomalies
    coordinates.append(vd.profile_coordinates((370e3,-8.53e6),(400e3,-8.49e6), size=1000, extra_coords=-300)[0])
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0]-20, south_anomaly[1]-15, np.full(1000, 8e8)))
    coordinates.append(vd.profile_coordinates((370e3,-8.53e6),(385e3,-8.49e6), size=1000, extra_coords=-300)[0])
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0]+5, south_anomaly[1]+5, np.full(1000, 8e8)))
    coordinates.append(vd.scatter_points([355e3, 410e3, -8.55e6, -8.50e6,], size=500, random_state=1,extra_coords=-1e3))
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0], south_anomaly[1], np.full(500, 5e9)))

    # Regional
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([200e3,500e3,-8.6e6,-8.2e6,], shape=(70,70), extra_coords=-30e3)])
    dipole_moments.append(eqs.angles_to_vector(regional[0], regional[1], np.full(4900, 1e11)))

    coordinates = np.concatenate(coordinates, axis=1)
    dipole_moments = np.concatenate(dipole_moments, axis=1)
    return coordinates, dipole_moments