"""
Module with custom functions for running synthetic datasets.
"""
import numpy as np
import verde as vd
import eqs_magnetics as eqs
import harmonica as hm

def icegrav_synthetic(source1, source2, source3, source4, source5, source6, source7, source8, regional):
    """
    Synthetic dataset associated with the ICEGRAV coordinates.
    Provide source directions specifed as [inclination, declination]. E.g. source1=[-60,60], where inclination=-60 and declination=60.
    """
    coordinates = []
    dipole_moments = []

    # SOURCE 1
    # Grid
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([1.28e6,1.32e6,3.39e6,3.41e6,], shape=(20,20), extra_coords=-1e3)])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(400,3e9), source1[0], source1[1])))
    # North
    coordinates.append(vd.profile_coordinates((1.284e6,3.411e6),(1.316e6,3.411e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.290e6,3.412e6),(1.310e6,3.412e6), size=12, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.296e6,3.413e6),(1.304e6,3.413e6), size=5, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,4e9), source1[0], source1[1])))
    # West
    coordinates.append(vd.profile_coordinates((1.278e6,3.392e6),(1.278e6,3.408e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.276e6,3.395e6),(1.276e6,3.405e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.274e6,3.397e6),(1.274e6,3.403e6), size=6, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(6,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.272e6,3.399e6),(1.272e6,3.401e6), size=2, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(2,4e9), source1[0], source1[1])))
    # South
    coordinates.append(vd.profile_coordinates((1.284e6,3.389e6),(1.316e6,3.389e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.290e6,3.388e6),(1.310e6,3.388e6), size=12, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.296e6,3.387e6),(1.304e6,3.387e6), size=5, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,4e9), source1[0], source1[1])))
    # East
    coordinates.append(vd.profile_coordinates((1.322e6,3.392e6),(1.322e6,3.408e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.324e6,3.395e6),(1.324e6,3.403e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.326e6,3.397e6),(1.326e6,3.403e6), size=6, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(6,4e9), source1[0], source1[1])))
    coordinates.append(vd.profile_coordinates((1.328e6,3.399e6),(1.328e6,3.401e6), size=2, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(2,4e9), source1[0], source1[1])))

    # SOURCE 2
    # Top
    coordinates.append(vd.profile_coordinates((1.24e6,3.254e6),(1.266e6,3.28e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.24e6,3.252e6),(1.268e6,3.28e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.24e6,3.25e6),(1.27e6,3.28e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.24e6,3.248e6),(1.27e6,3.278e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.24e6,3.246e6),(1.27e6,3.276e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source2[0], source2[1])))
    # Middle
    coordinates.append(vd.profile_coordinates((1.226e6,3.23e6),(1.27e6,3.274e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.226e6,3.228e6),(1.27e6,3.272e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.226e6,3.226e6),(1.27e6,3.27e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.226e6,3.224e6),(1.27e6,3.268e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.226e6,3.222e6),(1.27e6,3.266e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.226e6,3.22e6),(1.27e6,3.264e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.226e6,3.218e6),(1.27e6,3.262e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.227e6,3.216e6),(1.27e6,3.26e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source2[0], source2[1])))
    # Bottom
    coordinates.append(vd.profile_coordinates((1.228e6,3.216e6),(1.246e6,3.234e6), size=15, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(15,3e9), -source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.23e6,3.216e6),(1.246e6,3.232e6), size=15, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(15,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.232e6,3.216e6),(1.246e6,3.23e6), size=5, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,3e9), source2[0], source2[1])))
    coordinates.append(vd.profile_coordinates((1.234e6,3.216e6),(1.246e6,3.228e6), size=5, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,3e9), source2[0], source2[1])))

    # SOURCE 3
    # Grid
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([1.33e6,1.37e6,3.06e6,3.1e6,], shape=(20,20), extra_coords=-1e3)])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(400,5e9), source3[0], source3[1])))
    # North
    coordinates.append(vd.profile_coordinates((1.334e6,3.101e6),(1.366e6,3.101e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.340e6,3.102e6),(1.360e6,3.102e6), size=12, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.346e6,3.103e6),(1.354e6,3.103e6), size=5, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,5e9), source3[0], source3[1])))
    # East
    coordinates.append(vd.profile_coordinates((1.328e6,3.062e6),(1.328e6,3.098e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.326e6,3.065e6),(1.326e6,3.095e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.324e6,3.067e6),(1.324e6,3.093e6), size=8, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(8,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.322e6,3.069e6),(1.322e6,3.091e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.32e6,3.071e6),(1.32e6,3.089e6), size=6, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(6,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.318e6,3.075e6),(1.318e6,3.085e6), size=4, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(4,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.316e6,3.079e6),(1.316e6,3.081e6), size=2, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(2,5e9), source3[0], source3[1])))
    # South
    coordinates.append(vd.profile_coordinates((1.334e6,3.059e6),(1.366e6,3.059e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.340e6,3.058e6),(1.360e6,3.058e6), size=12, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.346e6,3.057e6),(1.354e6,3.057e6), size=5, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,5e9), source3[0], source3[1])))
    # East
    coordinates.append(vd.profile_coordinates((1.372e6,3.062e6),(1.372e6,3.098e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.374e6,3.065e6),(1.374e6,3.095e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.376e6,3.067e6),(1.376e6,3.093e6), size=8, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(8,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.378e6,3.071e6),(1.378e6,3.089e6), size=6, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(6,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.38e6,3.075e6),(1.38e6,3.085e6), size=4, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(4,5e9), source3[0], source3[1])))
    coordinates.append(vd.profile_coordinates((1.382e6,3.079e6),(1.382e6,3.081e6), size=2, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(2,5e9), source3[0], source3[1])))

    # SOURCE 4
    # Top
    coordinates.append(vd.profile_coordinates((1.46e6,2.91e6),(1.48e6,2.93e6), size=20, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.46e6,2.908e6),(1.482e6,2.93e6), size=20, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.46e6,2.906e6),(1.484e6,2.93e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.46e6,2.904e6),(1.486e6,2.93e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.46e6,2.902e6),(1.488e6,2.93e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.46e6,2.90e6),(1.49e6,2.93e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.46e6,2.898e6),(1.49e6,2.928e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.46e6,2.896e6),(1.49e6,2.926e6), size=30, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(30,3e9), source4[0], source4[1])))
    # Middle
    coordinates.append(vd.profile_coordinates((1.446e6,2.88e6),(1.49e6,2.924e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.446e6,2.878e6),(1.49e6,2.922e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.446e6,2.876e6),(1.49e6,2.92e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.446e6,2.874e6),(1.49e6,2.918e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.446e6,2.872e6),(1.49e6,2.916e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.446e6,2.87e6),(1.49e6,2.914e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.446e6,2.868e6),(1.49e6,2.912e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.446e6,2.866e6),(1.49e6,2.91e6), size=40, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(40,3e9), source4[0], source4[1])))
    # Bottom
    coordinates.append(vd.profile_coordinates((1.448e6,2.866e6),(1.466e6,2.884e6), size=15, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(15,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.45e6,2.866e6),(1.466e6,2.882e6), size=15, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(15,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.452e6,2.866e6),(1.466e6,2.88e6), size=5, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,3e9), source4[0], source4[1])))
    coordinates.append(vd.profile_coordinates((1.454e6,2.866e6),(1.466e6,2.878e6), size=5, extra_coords=-800)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,3e9), source4[0], source4[1])))

#     # SOURCE 5
    coordinates.append(vd.profile_coordinates((2.21e6,2.8185e6),(2.23e6,2.823e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.208e6,2.817e6),(2.234e6,2.823e6), size=15, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(15,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.206e6,2.8155e6),(2.24e6,2.8235e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.202e6,2.8135e6),(2.246e6,2.824e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.20e6,2.812e6),(2.25e6,2.824e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.20e6,2.811e6),(2.254e6,2.824e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.20e6,2.81e6),(2.257e6,2.824e6), size=25, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(25,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.20e6,2.809e6),(2.259e6,2.8235e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.202e6,2.8086e6),(2.26e6,2.8225e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.205e6,2.8086e6),(2.26e6,2.8215e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.209e6,2.8087e6),(2.259e6,2.8205e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))
    coordinates.append(vd.profile_coordinates((2.215e6,2.809e6),(2.257e6,2.819e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,6e9), source5[0], source5[1])))

    # SOURCE 6
    # Grid
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([2.23e6,2.27e6,2.755e6,2.775e6,], shape=(20,20), extra_coords=-1e3)])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(400,5e9), source6[0], source6[1])))
    # North
    coordinates.append(vd.profile_coordinates((2.234e6,2.776e6),(2.266e6,2.776e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,4e9), source6[0], source6[1])))
    coordinates.append(vd.profile_coordinates((2.240e6,2.777e6),(2.260e6,2.777e6), size=12, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,4e9), source6[0], source6[1])))
    coordinates.append(vd.profile_coordinates((2.246e6,2.778e6),(2.254e6,2.778e6), size=5, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,4e9), source6[0], source6[1])))
    # West
    coordinates.append(vd.profile_coordinates((2.228e6,2.757e6),(2.228e6,2.773e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,4e9), source6[0], source6[1])))
    coordinates.append(vd.profile_coordinates((2.226e6,2.760e6),(2.226e6,2.770e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,4e9), source6[0], source6[1])))
    # South
    coordinates.append(vd.profile_coordinates((2.234e6,2.754e6),(2.266e6,2.754e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,4e9), source6[0], source6[1])))
    coordinates.append(vd.profile_coordinates((2.240e6,2.753e6),(2.260e6,2.753e6), size=12, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(12,4e9), source6[0], source6[1])))
    coordinates.append(vd.profile_coordinates((2.246e6,2.752e6),(2.254e6,2.752e6), size=5, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(5,4e9), source6[0], source6[1])))
    # East
    coordinates.append(vd.profile_coordinates((2.272e6,2.757e6),(2.272e6,2.773e6), size=14, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(14,4e9), source6[0], source6[1])))
    coordinates.append(vd.profile_coordinates((2.274e6,2.760e6),(2.274e6,2.770e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,4e9), source6[0], source6[1])))
    coordinates.append(vd.profile_coordinates((2.276e6,2.762e6),(2.276e6,2.768e6), size=6, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(6,4e9), source6[0], source6[1])))

    # SOURCE 7
    coordinates.append(vd.profile_coordinates((2.222e6,2.720e6),(2.233e6,2.7225e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.22e6,2.7185e6),(2.24e6,2.723e6), size=10, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.218e6,2.717e6),(2.244e6,2.723e6), size=15, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(15,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.216e6,2.7155e6),(2.25e6,2.7235e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.212e6,2.7135e6),(2.256e6,2.724e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.21e6,2.712e6),(2.26e6,2.724e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.21e6,2.711e6),(2.264e6,2.724e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.21e6,2.71e6),(2.267e6,2.724e6), size=25, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(25,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.21e6,2.709e6),(2.269e6,2.7235e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.212e6,2.7086e6),(2.27e6,2.7225e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.215e6,2.7086e6),(2.27e6,2.7215e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.219e6,2.7087e6),(2.269e6,2.7205e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))
    coordinates.append(vd.profile_coordinates((2.225e6,2.709e6),(2.267e6,2.719e6), size=20, extra_coords=-1e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(20,3e9), source7[0], source7[1])))

    # SOURCE 8 (Large source)
    coordinates.append(vd.profile_coordinates((1.8e6,2.8e6),(2.0e6,3.2e6), size=1000, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(1000,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.82e6,2.83e6),(2.0e6,3.19e6), size=1000, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(1000,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.825e6,2.83e6),(2.0e6,3.18e6), size=1000, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(1000,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.83e6,2.83e6),(2.0e6,3.17e6), size=1000, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(1000,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.845e6,2.85e6),(1.99e6,3.14e6), size=900, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(900,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.85e6,2.85e6),(1.995e6,3.14e6), size=800, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(800,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.855e6,2.85e6),(2.0e6,3.14e6), size=900, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(900,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.853e6,2.83e6),(2.01e6,3.15e6), size=800, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(800,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.87e6,2.85e6),(2.02e6,3.15e6), size=900, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(900,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.955e6,3.0e6),(2.03e6,3.15e6), size=500, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(500,5e9), source8[0], source8[1])))
    coordinates.append(vd.profile_coordinates((1.96e6,3.0e6),(2.04e6,3.15e6), size=500, extra_coords=-5e3)[0])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(500,5e9), source8[0], source8[1])))

    # Regional
    coordinates.append([[1.5e6], [3.24e6], [-60e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(1e14, regional[0], regional[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[1.45e6], [3.24e6], [-60e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(1e14, regional[0], regional[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[1.7e6], [3.0e6], [-60e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(1e14, regional[0], regional[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[1.7e6], [2.95e6], [-60e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(1e14, regional[0], regional[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2.1e6], [2.8e6], [-60e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(1e14, regional[0], regional[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([[2.05e6], [2.8e6], [-60e3]])
    _dipole_moment_e, _dipole_moment_n, _dipole_moment_u = hm.magnetic_angles_to_vec(1e14, regional[0], regional[1])
    dipole_moments.append(np.array([[_dipole_moment_e], [_dipole_moment_n], [_dipole_moment_u]]))
    coordinates.append([np.asarray(c).ravel() for c in vd.grid_coordinates([1e6,2.5e6,2.5e6,3.5e6,], shape=(100,100), extra_coords=-60e3)])
    dipole_moments.append(np.array(hm.magnetic_angles_to_vec(np.full(10000, 9e11), regional[0], regional[1])))

    coordinates = np.concatenate(coordinates, axis=1)
    dipole_moments = np.concatenate(dipole_moments, axis=1)
    return coordinates, dipole_moments


def simple_synthetic(dike1, dike2, point1, point2, point3, point4, regional ):
    """
    Simple synthetic dataset associated with the Victoria Land coordinates.
    Provide source directions specifed as [inclination, declination]. E.g. dike1=[70,60], where inclination=70 and declination=60.
    """
    dipole_moments = []
    coordinates = []
    dike_moment_magnitude = 10e7
    # Dike NE-SW
    coordinates.append(vd.profile_coordinates((-20e3, -5e3), (20e3, 12e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dike1[0], dike1[1], np.full(1000, dike_moment_magnitude)))
    # Dike NW-SE
    coordinates.append(vd.profile_coordinates((20e3, -10e3), (-20e3, 25e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dike2[0], dike2[1], np.full(1000, dike_moment_magnitude)))
    # Dike small
    coordinates.append(vd.profile_coordinates((20e3, -4e3), (4e3, 3e3), size=1000, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dike2[0], dike2[1], np.full(1000, dike_moment_magnitude)))
    # Dike very small
    coordinates.append(vd.profile_coordinates((3e3, 3.5e3), (-0.5e3, 5.5e3), size=100, extra_coords=0)[0])
    dipole_moments.append(eqs.angles_to_vector(dike2[0], dike2[1], np.full(100, dike_moment_magnitude)))
    # point source top left
    coordinates.append([[-7500], [7000], [-350]])
    dipole_moments.append(eqs.angles_to_vector(point1[0], point1[1], 1e10))
    # point source centre
    coordinates.append([[0], [-100], [-1e3]])
    dipole_moments.append(eqs.angles_to_vector(point2[0], point2[1], 5e10))
    # point source bottom left
    coordinates.append([[-8000], [-6000], [-800]])
    dipole_moments.append(eqs.angles_to_vector(point3[0], point3[1], 5e10))
    # point source bottom right
    coordinates.append([[7500], [-7500], [-500]])
    dipole_moments.append(eqs.angles_to_vector(point4[0], point4[1], 2e10))    
    # regional
    coordinates.append([[2e3, -5e3], [-9e3, 5e3], [-8e3, -8e3]])
    dipole_moments.append(eqs.angles_to_vector(regional[0], regional[1], np.full(2, 1e13)))

    coordinates = np.concatenate(coordinates, axis=1)
    dipole_moments = np.concatenate(dipole_moments, axis=1)
    return coordinates, dipole_moments

def complicated_synthetic(largest_anomaly, grid_anomaly, scatter_anomaly, north_anomaly, south_anomaly, regional):
    """
    Complicated synthetic dataset associated with the Victoria Land coordinates.
    Provide source directions specifed as [inclination, declination]. E.g. dike1=[70,60], where inclination=70 and declination=60.
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