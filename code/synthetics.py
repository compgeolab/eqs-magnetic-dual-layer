"""
Module with custom functions for running synthetic datasets.
"""
import numpy as np
import verde as vd
import eqs_magnetics as eqs
import harmonica as hm

# def generate_dm(magnitude, source, size):
#     dipole_moments = []
#     for i in range(size):
#         _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(np.full(size, magnitude), source[0], source[1])
#         dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
#     return np.array(dipole_moments)


# def append_coords_and_dm(coordinates, dipole_moments, coord_data, dm_data):
#     coordinates.append(np.asarray(coord_data))
#     dipole_moments.append(np.asarray(dm_data))

# def create_source_profile(source, coordinates, dipole_moments, profiles):
#     for profile in profiles:
#         coords = vd.profile_coordinates(
#             profile['first'],
#             profile['last'],
#             size=int(profile['size']),
#             extra_coords=profile['height'],
#         )[0]
#         append_coords_and_dm(
#             coordinates,
#             dipole_moments,
#             coords,
#             generate_dm(profile['magnitude'], source, len(coords)),
#         )

# def create_source_grid(source, coordinates, dipole_moments, grid_profiles):
#     for profile in grid_profiles:
#         coords = [np.asarray(c).ravel() for c in vd.grid_coordinates(
#             profile['WESN'],
#             shape=profile['shape'],
#             extra_coords=profile['height'],
#         )]
#         for coord in coords:
#             append_coords_and_dm(
#                 coordinates,
#                 dipole_moments,
#                 coord,
#                 generate_dm(
#                     profile['magnitude'],
#                     source,
#                     len(coord),
#                 ),
#             )
    
# def icegrav_synthetic(source1, source2, source3, source4, dyke1, dyke2, dipole, regional_dipole, regional):
#     """
#     Synthetic dataset associated with the ICEGRAV coordinates.
#     Provide source directions specifed as [inclination, declination]. E.g. source1=[-60,60], where inclination=-60 and declination=60.
#     """
#     coordinates = []
#     dipole_moments = []
    
#     # Source 1
#     source1_height = -6e3
#     source1_magnitude = 2e10
#     source1_grid = [
#         {'WESN': [1.91e6,1.95e6,3.015e6,3.035e6],
#          'shape': (20,20),
#          'height': source1_height,
#          'magnitude': (source1_magnitude/2)}
#     ]
#     source1_profiles = [
#         {'first': (1.914e6,3.036e6), 'last': (1.946e6,3.036e6), 'size': 14, 'height': source1_height, 'magnitude': source1_magnitude},
#         {'first': (1.92e6,3.037e6), 'last': (1.94e6,3.037e6), 'size': 12, 'height': source1_height, 'magnitude': source1_magnitude},
#         {'first': (1.926e6,3.038e6), 'last': (1.934e6,3.038e6), 'size': 5, 'height': source1_height, 'magnitude': source1_magnitude},
#         {'first': (1.908e6,3.017e6), 'last': (1.908e6,3.033e6), 'size': 14, 'height': source1_height, 'magnitude': source1_magnitude},
#         {'first': (1.914e6,3.014e6), 'last': (1.946e6,3.014e6), 'size': 14, 'height': source1_height, 'magnitude': source1_magnitude},
#         {'first': (1.92e6,3.013e6), 'last': (1.94e6,3.013e6), 'size': 12, 'height': source1_height, 'magnitude': source1_magnitude},
#         {'first': (1.926e6,3.012e6), 'last': (1.934e6,3.012e6), 'size': 5, 'height': source1_height, 'magnitude': source1_magnitude},
#         {'first': (1.952e6,3.017e6), 'last': (1.952e6,3.033e6), 'size': 14, 'height': source1_height, 'magnitude': source1_magnitude},
#         {'first': (1.954e6,3.020e6), 'last': (1.954e6,3.029e6), 'size': 10, 'height': source1_height, 'magnitude': source1_magnitude}
#     ]
#     create_source_profile(source1, coordinates, dipole_moments, source1_profiles)
#     create_source_grid(source1, coordinates, dipole_moments, source1_grid)
    
#     for c in coordinates:
#         print(np.shape(c))  # Check the shapes
#     for dm in dipole_moments:
#         print(np.shape(dm))
    
#     # Source 2
#     source2_height = -800
#     source2_magnitude = 3e9
#     source2_size=30
#     source2_profiles = [
#         {'first': (1.96e6,2.974e6), 'last': (1.986e6,3.00e6), 'size': source2_size, 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.96e6,2.972e6), 'last': (1.988e6,3.00e6), 'size': source2_size, 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.96e6,2.97e6), 'last': (1.99e6,3.00e6), 'size': source2_size, 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.96e6,2.968e6), 'last': (1.99e6,2.998e6), 'size': source2_size, 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.96e6,2.966e6), 'last': (1.99e6,2.996e6), 'size': source2_size, 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.946e6,2.95e6), 'last': (1.99e6,2.994e6), 'size': (source2_size+10), 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.946e6,2.948e6), 'last': (1.99e6,2.992e6), 'size': (source2_size+10), 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.946e6,2.946e6), 'last': (1.99e6,2.99e6), 'size': (source2_size+10), 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.946e6,2.944e6), 'last': (1.99e6,2.988e6), 'size': (source2_size+10), 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.946e6,2.942e6), 'last': (1.99e6,2.986e6), 'size': (source2_size+10), 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.946e6,2.94e6), 'last': (1.99e6,2.984e6), 'size': (source2_size+10), 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.946e6,2.948e6), 'last': (1.99e6,2.982e6), 'size': (source2_size+10), 'height': source2_height, 'magnitude': source2_magnitude},
#         {'first': (1.947e6,2.946e6), 'last': (1.99e6,2.98e6), 'size': (source2_size+10), 'height': source2_height, 'magnitude': source2_magnitude},
#         ]
#     create_source_profile(source2, coordinates, dipole_moments, source2_profiles)
    
#     #Source 3
#     source3_height = -900
#     source3_magnitude = 5e9
#     source3_size=20
#     source3_profiles = [
#         {'first': (2.21e6,2.8185e6), 'last': (2.23e6,2.823e6), 'size': (source3_size-10), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.208e6,2.817e6), 'last': (2.234e6,2.823e6), 'size': (source3_size-5), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.206e6,2.8155e6), 'last': (2.24e6,2.8235e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.202e6,2.8135e6), 'last': (2.246e6,2.824e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.20e6,2.812e6), 'last': (2.25e6,2.824e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.20e6,2.811e6), 'last': (2.254e6,2.824e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.20e6,2.81e6), 'last': (2.257e6,2.824e6), 'size': (source3_size+5), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.20e6,2.809e6), 'last': (2.259e6,2.8235e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.202e6,2.8086e6), 'last': (2.26e6,2.8225e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.205e6,2.8086e6), 'last': (2.26e6,2.8215e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.209e6,2.8087e6), 'last': (2.259e6,2.8205e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},
#         {'first': (2.215e6,2.809e6), 'last': (2.257e6,2.819e6), 'size': (source3_size), 'height': source3_height, 'magnitude': source3_magnitude},   
#     ]
#     create_source_profile(source3, coordinates, dipole_moments, source3_profiles)
    
#     # Source 4
#     source4_height = -8e3
#     source4_magnitude = 1e10
#     source4_grid = [
#         {'WESN': [2.24e6,2.265e6,2.715e6,2.735e6],
#          'shape': (20,20),
#          'height': source4_height,
#          'magnitude': source4_magnitude}
#     ]
#     source4_profiles = [
#         {'first': (2.236e6,2.736e6), 'last': (2.266e6,2.736e6), 'size': 14, 'height': source4_height, 'magnitude': source4_magnitude},
#         {'first': (2.220e6,2.737e6), 'last': (2.260e6,2.737e6), 'size': 12, 'height': source4_height, 'magnitude': source4_magnitude},
#         {'first': (2.226e6,2.738e6), 'last': (2.254e6,2.738e6), 'size': 5, 'height': source4_height, 'magnitude': source4_magnitude},
#         {'first': (2.238e6,2.734e6), 'last': (2.238e6,2.713e6), 'size': 14, 'height': source4_height, 'magnitude': source4_magnitude},
#         {'first': (2.240e6,2.711e6), 'last': (2.266e6,2.711e6), 'size': 14, 'height': source4_height, 'magnitude': source4_magnitude},
#         {'first': (2.244e6,2.713e6), 'last': (2.260e6,2.713e6), 'size': 12, 'height': source4_height, 'magnitude': source4_magnitude},
#         {'first': (2.246e6,2.715e6), 'last': (2.264e6,2.715e6), 'size': 5, 'height': source4_height, 'magnitude': source4_magnitude}, 
#     ]
#     create_source_profile(source4, coordinates, dipole_moments, source4_profiles)
#     create_source_grid(source4, coordinates, dipole_moments, source4_grid)
    
#     # Dyke 1
#     dyke1_height = -1e3
#     dyke1_magnitude = 1e9
#     dyke1_size=500
#     dyke1_profiles = [
#         {'first': (2.18e6,2.9e6), 'last': (2.205e6,3.0e6), 'size': (dyke1_size), 'height': dyke1_height, 'magnitude': dyke1_magnitude},
#         {'first': (2.185e6,2.9e6), 'last': (2.21e6,3.0e6), 'size': (dyke1_size), 'height': dyke1_height, 'magnitude': dyke1_magnitude},
#     ]
#     create_source_profile(dyke1, coordinates, dipole_moments, dyke1_profiles)

#     # Dyke 2
#     dyke2_height = -5e3
#     dyke2_magnitude = 2e9
#     dyke2_size=1e3
#     dyke2_profiles = [
#         {'first': (2.16e6,2.76e6), 'last': (2.26e6,2.98e6), 'size': (dyke2_size), 'height': dyke2_height, 'magnitude': dyke2_magnitude},
#         {'first': (2.165e6,2.76e6), 'last': (2.261e6,2.98e6), 'size': (dyke2_size), 'height': dyke2_height, 'magnitude': dyke2_magnitude},
#         {'first': (2.17e6,2.76e6), 'last': (2.262e6,2.98e6), 'size': (dyke2_size), 'height': dyke2_height, 'magnitude': dyke2_magnitude},
#         {'first': (2.185e6,2.78e6), 'last': (2.263e6,2.98e6), 'size': (dyke2_size-10), 'height': dyke2_height, 'magnitude': dyke2_magnitude},
#         {'first': (2.19e6,2.78e6), 'last': (2.264e6,2.98e6), 'size': (dyke2_size-20), 'height': dyke2_height, 'magnitude': dyke2_magnitude},
#         {'first': (2.195e6,2.78e6), 'last': (2.265e6,2.98e6), 'size': (dyke2_size-10), 'height': dyke2_height, 'magnitude': dyke2_magnitude},   
#     ]
#     create_source_profile(dyke2, coordinates, dipole_moments, dyke2_profiles)

#     # Small dipoles
#     small_dipoles_coords = [
#         [[1.95e6], [2.785e6], [-500]],
#         [[2.1e6], [3.011e6], [-500]],
#         [[2.11e6], [2.955e6], [-500]],
#         [[2.15e6], [2.75e6], [-500]],
#     ]
#     append_coords_and_dm(
#             coordinates,
#             dipole_moments,
#             small_dipoles_coords,
#             generate_dm(5e10, dipole, len(small_dipoles_coords)),
#         )
    
#     # Regional Dipole
#     regional_dipole_height = -70e3
#     regional_coordinates = [
#         [[2035e3], [2925e3], [regional_dipole_height]],
#         [[2050e3], [2925e3], [regional_dipole_height]],
#         [[2020e3], [2910e3], [regional_dipole_height]],
#         [[2035e3], [2910e3], [regional_dipole_height]],
#         [[2050e3], [2910e3], [regional_dipole_height]],
#         [[2075e3], [2910e3], [regional_dipole_height]],
#         [[2020e3], [2895e3], [regional_dipole_height]],
#         [[2035e3], [2895e3], [regional_dipole_height]],
#         [[2050e3], [2895e3], [regional_dipole_height]],
#         [[2075e3], [2915e3], [regional_dipole_height]],
#         [[2005e3], [2880e3], [regional_dipole_height]],
#         [[2020e3], [2880e3], [regional_dipole_height]],
#         [[2035e3], [2880e3], [regional_dipole_height]],
#         [[2050e3], [2880e3], [regional_dipole_height]],
#         [[2075e3], [2880e3], [regional_dipole_height]],
#         [[2090e3], [2880e3], [regional_dipole_height]],
#         [[2100e3], [2880e3], [regional_dipole_height]],
#         [[2005e3], [2865e3], [regional_dipole_height]],
#         [[2020e3], [2865e3], [regional_dipole_height]],
#         [[2035e3], [2865e3], [regional_dipole_height]],
#         [[2050e3], [2865e3], [regional_dipole_height]],
#         [[2075e3], [2865e3], [regional_dipole_height]],
#         [[2090e3], [2865e3], [regional_dipole_height]],
#         [[2100e3], [2865e3], [regional_dipole_height]],
#         [[2020e3], [2850e3], [regional_dipole_height]],
#         [[2035e3], [2850e3], [regional_dipole_height]],
#         [[2050e3], [2850e3], [regional_dipole_height]],
#         [[2075e3], [2850e3], [regional_dipole_height]],
#         [[2020e3], [2850e3], [regional_dipole_height]],
#         [[2035e3], [2850e3], [regional_dipole_height]],
#         [[2050e3], [2835e3], [regional_dipole_height]],
#         [[2065e3], [2835e3], [regional_dipole_height]],
#         [[2035e3], [2820e3], [regional_dipole_height]],
#         [[2050e3], [2820e3], [regional_dipole_height]]
#     ]
#     append_coords_and_dm(
#             coordinates,
#             dipole_moments,
#             regional_coordinates,
#             generate_dm(2e13, regional_dipole, len(regional_coordinates)),
#         )
    
#     # Regional
#     region = [1.85e6,2.35e6,2.54e6,3.1e6]
#     easting, northing = vd.grid_coordinates(region, shape=(30,30))
#     upward = vd.synthetic.CheckerBoard(region=region, amplitude=15e3, w_east=0.25e6, w_north=0.25e6).predict((easting, northing)) + -60e3
#     regional_coords = (easting, northing, upward)
#     for i, c in enumerate(regional_coords):
#         eqs.contaminate(c, standard_deviation=5, random_state=i)
#     coordinates.append([np.asarray(c).ravel() for c in regional_coords])
#     dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(900,5e12), regional[0], regional[1])))

#     coordinates = np.concatenate(coordinates, axis=1)
#     dipole_moments = np.concatenate(dipole_moments, axis=1)
#     return coordinates, dipole_moments
    
    
    
def icegrav_synthetic(source1, source2, source3, source4, dyke1, dyke2, dipole, regional_dipole, regional):
    """
    Synthetic dataset associated with the ICEGRAV coordinates.
    Provide source directions specifed as [inclination, declination]. E.g. source1=[-60,60], where inclination=-60 and declination=60.
    """
    coordinates = []
    dipole_moments = []

    # SOURCE 1
    # Grid
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([1.91e6,1.95e6,3.015e6,3.035e6], shape=(20,20), extra_coords=-6e3)])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(400,1e10), source1[0], source1[1])))
    # North
    coordinates.append(vd.profile_coordinates((1.914e6,3.036e6),(1.946e6,3.036e6), size=14, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,2e10), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.92e6,3.037e6),(1.94e6,3.037e6), size=12, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,2e10), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.926e6,3.038e6),(1.934e6,3.038e6), size=5, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,2e10), source1[0], source1[1])))
    # West
    coordinates.append(vd.profile_coordinates((1.908e6,3.017e6),(1.908e6,3.033e6), size=14, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,2e10), source1[0], source1[1])))
    # South
    coordinates.append(vd.profile_coordinates((1.914e6,3.014e6),(1.946e6,3.014e6), size=14, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,2e10), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.92e6,3.013e6),(1.94e6,3.013e6), size=12, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,2e10), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.926e6,3.012e6),(1.934e6,3.012e6), size=5, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,2e10), source1[0], source1[1])))
    # East
    coordinates.append(vd.profile_coordinates((1.952e6,3.017e6),(1.952e6,3.033e6), size=14, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,2e10), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.954e6,3.020e6),(1.954e6,3.029e6), size=10, extra_coords=-6e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,2e10), source1[0], source1[1])))

    # SOURCE 2
    # Top
    coordinates.append(vd.profile_coordinates((1.96e6,2.974e6),(1.986e6,3.00e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.96e6,2.972e6),(1.988e6,3.00e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.96e6,2.97e6),(1.99e6,3.00e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.96e6,2.968e6),(1.99e6,2.998e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.96e6,2.966e6),(1.99e6,2.996e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    # Middle
    coordinates.append(vd.profile_coordinates((1.946e6,2.95e6),(1.99e6,2.994e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.946e6,2.948e6),(1.99e6,2.992e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.946e6,2.946e6),(1.99e6,2.99e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.946e6,2.944e6),(1.99e6,2.988e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.946e6,2.942e6),(1.99e6,2.986e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.946e6,2.94e6),(1.99e6,2.984e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.946e6,2.948e6),(1.99e6,2.982e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.947e6,2.946e6),(1.99e6,2.98e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))

    # SOURCE 3
    coordinates.append(vd.profile_coordinates((2.21e6,2.8185e6),(2.23e6,2.823e6), size=10, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.208e6,2.817e6),(2.234e6,2.823e6), size=15, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(15,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.206e6,2.8155e6),(2.24e6,2.8235e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.202e6,2.8135e6),(2.246e6,2.824e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.20e6,2.812e6),(2.25e6,2.824e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.20e6,2.811e6),(2.254e6,2.824e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.20e6,2.81e6),(2.257e6,2.824e6), size=25, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(25,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.20e6,2.809e6),(2.259e6,2.8235e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.202e6,2.8086e6),(2.26e6,2.8225e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.205e6,2.8086e6),(2.26e6,2.8215e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.209e6,2.8087e6),(2.259e6,2.8205e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((2.215e6,2.809e6),(2.257e6,2.819e6), size=20, extra_coords=-900)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,5e9), source3[0], source3[1])))

    # SOURCE 4
    # Grid
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([2.24e6,2.265e6,2.715e6,2.735e6], shape=(20,20), extra_coords=-8e3)])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(400,9e9), source4[0], source4[1])))
    # North
    coordinates.append(vd.profile_coordinates((2.236e6,2.736e6),(2.266e6,2.736e6), size=14, extra_coords=-8e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,1e10), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((2.220e6,2.737e6),(2.260e6,2.737e6), size=12, extra_coords=-8e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,1e10), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((2.226e6,2.738e6),(2.254e6,2.738e6), size=5, extra_coords=-8e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,1e10), source4[0], source4[1])))
    # West
    coordinates.append(vd.profile_coordinates((2.238e6,2.734e6),(2.238e6,2.713e6), size=14, extra_coords=-8e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,1e10), source4[0], source4[1])))
    # South
    coordinates.append(vd.profile_coordinates((2.240e6,2.711e6),(2.266e6,2.711e6), size=14, extra_coords=-8e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,1e10), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((2.244e6,2.713e6),(2.260e6,2.713e6), size=12, extra_coords=-8e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,1e10), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((2.246e6,2.715e6),(2.264e6,2.715e6), size=5, extra_coords=-8e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,1e10), source4[0], source4[1])))

    # dyke 1
    coordinates.append(vd.profile_coordinates((2.18e6,2.9e6),(2.205e6,3.0e6), size=500, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(500,1e9), dyke1[0], dyke1[1])))
    coordinates.append(vd.profile_coordinates((2.185e6,2.9e6),(2.21e6,3.0e6), size=500, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(500,1e9), dyke1[0], dyke1[1])))
    
    # dyke 2
    coordinates.append(vd.profile_coordinates((2.16e6,2.76e6),(2.26e6,2.98e6), size=1000, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(1000,2e9), dyke2[0], dyke2[1])))
    coordinates.append(vd.profile_coordinates((2.165e6,2.76e6),(2.261e6,2.98e6), size=1000, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(1000,2e9), dyke2[0], dyke2[1])))
    coordinates.append(vd.profile_coordinates((2.17e6,2.76e6),(2.262e6,2.98e6), size=1000, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(1000,2e9), dyke2[0], dyke2[1])))
    coordinates.append(vd.profile_coordinates((2.185e6,2.78e6),(2.263e6,2.98e6), size=900, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(900,2e9), dyke2[0], dyke2[1])))
    coordinates.append(vd.profile_coordinates((2.19e6,2.78e6),(2.264e6,2.98e6), size=800, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(800,2e9), dyke2[0], dyke2[1])))
    coordinates.append(vd.profile_coordinates((2.195e6,2.78e6),(2.265e6,2.98e6), size=900, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(900,2e9), dyke2[0], dyke2[1])))
    
    # Small dipoles
    coordinates.append([[1.95e6], [2.785e6], [-500]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(5e10, dipole[0], dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2.1e6], [3.011e6], [-500]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(5e10, dipole[0], dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2.11e6], [2.955e6], [-500]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(5e10, dipole[0], dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2.15e6], [2.75e6], [-500]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(5e10, dipole[0], dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    
    
    # Regional dipole
    coordinates.append([[2035e3], [2925e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2050e3], [2925e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2020e3], [2910e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2035e3], [2910e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2050e3], [2910e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2075e3], [2910e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2020e3], [2895e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2035e3], [2895e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2050e3], [2895e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2075e3], [2915e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2005e3], [2880e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2020e3], [2880e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2035e3], [2880e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2050e3], [2880e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2075e3], [2880e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2090e3], [2880e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2100e3], [2880e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2005e3], [2865e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2020e3], [2865e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2035e3], [2865e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2050e3], [2865e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2075e3], [2865e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2090e3], [2865e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2100e3], [2865e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2020e3], [2850e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2035e3], [2850e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2050e3], [2850e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2075e3], [2850e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2020e3], [2850e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2035e3], [2850e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2050e3], [2835e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2065e3], [2835e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2035e3], [2820e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2050e3], [2820e3], [-70e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(2e13, regional_dipole[0], regional_dipole[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    
    # Regional
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