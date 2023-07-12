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