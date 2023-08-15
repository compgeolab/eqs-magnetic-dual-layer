"""
Module with custom functions for running synthetic datasets.
"""
import numpy as np
import verde as vd
import eqs_magnetics as eqs

def simple_synthetic(dike1, dike2, point1, point2, point3, point4, regional ):
    """
    Simple synthetic
    Provide source directions specifed as [inclination, declination]. E.g. dike1=[70,60], where inclination=70 and declination=60.
    """
    dipole_moments = []
    source_coordinates = []
    dike_moment_magnitude = 10e7
    # Dike NE-SW
    source_coordinates.append(vd.profile_coordinates((-20e3, -5e3), (20e3, 12e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dike1[0], dike1[1], np.full(1000, dike_moment_magnitude)))
    # Dike NW-SE
    source_coordinates.append(vd.profile_coordinates((20e3, -10e3), (-20e3, 25e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dike2[0], dike2[1], np.full(1000, dike_moment_magnitude)))
    # Dike small
    source_coordinates.append(vd.profile_coordinates((20e3, -4e3), (4e3, 3e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dike2[0], dike2[1], np.full(1000, dike_moment_magnitude)))
    # Dike very small
    source_coordinates.append(vd.profile_coordinates((3e3, 3.5e3), (-0.5e3, 5.5e3), size=100, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dike2[0], dike2[1], np.full(100, dike_moment_magnitude)))
    # point source top left
    source_coordinates.append([[-7500], [7000], [-350]])
    dipole_moments.append(eqs.angles_to_vector(point1[0], point1[1], 1e10))
    # point source centre
    source_coordinates.append([[0], [-100], [-1e3]])
    dipole_moments.append(eqs.angles_to_vector(point2[0], point2[1], 5e10))
    # point source bottom left
    source_coordinates.append([[-8000], [-6000], [-800]])
    dipole_moments.append(eqs.angles_to_vector(point3[0], point3[1], 5e10))
    # point source bottom right
    source_coordinates.append([[7500], [-7500], [-500]])
    dipole_moments.append(eqs.angles_to_vector(point4[0], point4[1], 2e10))    
    # regional
    source_coordinates.append([[2e3, -5e3], [-9e3, 5e3], [-8e3, -8e3]])
    dipole_moments.append(eqs.angles_to_vector(regional[0], regional[1], np.full(2, 1e13)))

    source_coordinates = np.concatenate(source_coordinates, axis=1)
    dipole_moments = np.concatenate(dipole_moments, axis=1)
    return source_coordinates, dipole_moments

def complicated_synthetic(largest_anomaly, grid_anomaly, scatter_anomaly, north_anomaly, south_anomaly, regional):
    dipole_moments = []
    source_coordinates = []
    # Largest source
    # 1st part
    source_coordinates.append(vd.profile_coordinates((260e3,-8.25e6),(310e3,-8.27e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((260e3,-8.255e6),(310e3,-8.275e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((270e3,-8.26e6),(310e3,-8.28e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((280e3,-8.27e6),(310e3,-8.285e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((280e3,-8.29e6),(325e3,-8.29e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    # 2nd part
    source_coordinates.append(vd.profile_coordinates((285e3,-8.29e6),(380e3,-8.320e6), size=2000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(2000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((285e3,-8.295e6),(380e3,-8.325e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    # 3rd part
    source_coordinates.append(vd.profile_coordinates((310e3,-8.31e6),(380e3,-8.33e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((300e3,-8.315e6),(380e3,-8.34e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((290e3,-8.32e6),(395e3,-8.345e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((290e3,-8.325e6),(400e3,-8.35e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((290e3,-8.33e6),(395e3,-8.355e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    # 4th part
    source_coordinates.append(vd.profile_coordinates((345e3,-8.35e6),(395e3,-8.365e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((340e3,-8.36e6),(400e3,-8.375e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    source_coordinates.append(vd.profile_coordinates((345e3,-8.365e6),(400e3,-8.38e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 5e8)))
    # 5th part
    source_coordinates.append(vd.profile_coordinates((360e3,-8.37e6),(400e3,-8.385e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((365e3,-8.38e6),(400e3,-8.39e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((370e3,-8.385e6),(405e3,-8.395e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((375e3,-8.39e6),(405e3,-8.40e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((375e3,-8.395e6),(410e3,-8.405e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    # 6th part
    source_coordinates.append(vd.profile_coordinates((370e3,-8.40e6),(410e3,-8.41e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((370e3,-8.405e6),(415e3,-8.415e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((370e3,-8.41e6),(415e3,-8.42e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((370e3,-8.415e6),(420e3,-8.425e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    # 7th part
    source_coordinates.append(vd.profile_coordinates((390e3,-8.42e6),(420e3,-8.43e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(85, 75, np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((395e3,-8.425e6),(425e3,-8.435e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((395e3,-8.43e6),(425e3,-8.44e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 2e8)))
    source_coordinates.append(vd.profile_coordinates((395e3,-8.435e6),(430e3,-8.445e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 1e8)))
    # 8th part
    source_coordinates.append(vd.profile_coordinates((400e3,-8.44e6),(440e3,-8.45e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    source_coordinates.append(vd.profile_coordinates((405e3,-8.445e6),(435e3,-8.455e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    source_coordinates.append(vd.profile_coordinates((415e3,-8.45e6),(430e3,-8.46e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    source_coordinates.append(vd.profile_coordinates((418e3,-8.455e6),(425e3,-8.465e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    source_coordinates.append(vd.profile_coordinates((419e3,-8.46e6),(422e3,-8.47e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    source_coordinates.append(vd.profile_coordinates((420e3,-8.46e6),(422e3,-8.47e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))
    source_coordinates.append(vd.profile_coordinates((420e3,-8.465e6),(420e3,-8.475e6), size=4000, extra_coords=-5e3)[0])
    dipole_moments.append(eqs.angles_to_vector(largest_anomaly[0], largest_anomaly[1], np.full(4000, 9e7)))

    # North Anomalies
    source_coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([340e3,390e3,-8.26e6,-8.20e6,], shape=(100,100), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(north_anomaly[0], north_anomaly[1], np.full(10000, 5e8)))
    source_coordinates.append(vd.scatter_points([250e3, 430e3, -8.28e6, -8.20e6,], size=1000, random_state=0, extra_coords=-1e3))
    dipole_moments.append(eqs.angles_to_vector(north_anomaly[0]-10, north_anomaly[1]-10, np.full(1000, 1e10)))
    source_coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([420e3,430e3,-8.315e6,-8.30e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(north_anomaly[0], north_anomaly[1], np.full(2500, 9e8)))

    # West scatter anomalies
    source_coordinates.append(vd.scatter_points([250e3, 290e3, -8.34e6, -8.30e6,], size=200, random_state=10,extra_coords=-100))
    dipole_moments.append(eqs.angles_to_vector(scatter_anomaly[0]+10, scatter_anomaly[1]+15, np.full(200, 5e9)))

    # Grid anomaly 1
    source_coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([248e3,270e3,-8.38e6,-8.36e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(grid_anomaly[0], grid_anomaly[1], np.full(2500, 9e8)))
    # Grid anomaly 2
    source_coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([290e3,310e3,-8.38e6,-8.36e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(grid_anomaly[0], grid_anomaly[1], np.full(2500, 9e8)))
    # Grid anomaly 3
    source_coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([330e3,350e3,-8.40e6,-8.38e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(grid_anomaly[0], grid_anomaly[1], np.full(2500, 9e8)))

    # Middle scatter anomaly
    source_coordinates.append(vd.scatter_points([240e3, 260e3, -8.42e6, -8.38e6,], size=250, random_state=1,extra_coords=-100))
    dipole_moments.append(eqs.angles_to_vector(scatter_anomaly[0], scatter_anomaly[1], np.full(250, 3e9)))
    source_coordinates.append(vd.scatter_points([310e3, 400e3, -8.46e6, -8.41e6,], size=1000, random_state=2,extra_coords=-100))
    dipole_moments.append(eqs.angles_to_vector(scatter_anomaly[0], scatter_anomaly[1], np.full(1000, 5e9)))

    # South-West anomalies
    source_coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([270e3,300e3,-8.47e6,-8.45e6,], shape=(50,50), extra_coords=-200)])
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0], south_anomaly[1], np.full(2500, 2e9)))
    source_coordinates.append(vd.profile_coordinates((260e3,-8.54e6),(300e3,-8.48e6), size=1000, extra_coords=-6e3)[0])
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0]+15, south_anomaly[1]+5, np.full(1000, 5e9)))
    source_coordinates.append(vd.scatter_points([250e3, 275e3, -8.50e6, -8.485e6,], size=750, random_state=1,extra_coords=-1e3))
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0]-15, south_anomaly[1]-10, np.full(750, 1e9)))

    # South-East Anomalies
    source_coordinates.append(vd.profile_coordinates((370e3,-8.53e6),(400e3,-8.49e6), size=1000, extra_coords=-300)[0])
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0]-20, south_anomaly[1]-15, np.full(1000, 8e8)))
    source_coordinates.append(vd.profile_coordinates((370e3,-8.53e6),(385e3,-8.49e6), size=1000, extra_coords=-300)[0])
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0]+5, south_anomaly[1]+5, np.full(1000, 8e8)))
    source_coordinates.append(vd.scatter_points([355e3, 410e3, -8.55e6, -8.50e6,], size=500, random_state=1,extra_coords=-1e3))
    dipole_moments.append(eqs.angles_to_vector(south_anomaly[0], south_anomaly[1], np.full(500, 5e9)))

    # Regional
    source_coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([200e3,500e3,-8.6e6,-8.2e6,], shape=(70,70), extra_coords=-30e3)])
    dipole_moments.append(eqs.angles_to_vector(regional[0], regional[1], np.full(4900, 1e11)))

    source_coordinates = np.concatenate(source_coordinates, axis=1)
    dipole_moments = np.concatenate(dipole_moments, axis=1)
    return source_coordinates, dipole_moments