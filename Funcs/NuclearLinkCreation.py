import copy
import numbers
import numpy as np


def nuc_nuc_link_creation(set_of_all_nuc, coordinates_of_interest, r, set_angles, index, output):
    """
    This function determines the nearest neighbors to a given nucleus on the  basis of spatial proximity.
    The maximum distance for consideration as a nearest neighbor  is 1.5x the mean distance between
    nuclei within that core.

    Note: This function is heavily commented, as it would otherwise be hard to follow.

    input: set_of_all_nuc- array storing all x, y coordinates | coordinates of interest - x, y coordinates of centroid nuclei
        r - maximum permissible internuclear distance (1.5x mean) | set_angles - array of pi/12 sized sections of unit circle
            | index - index of nucleus of interest | output - dictionary to keep track of angle section/nuclei location relationship
    output: final_dexs - indices of nearest neighbors | final vals - nearest neighor values
    """
    if not isinstance(set_of_all_nuc, np.ndarray):
        print('ERROR (nuc_nuc_link_creation): set_of_all_nuc object should be of type numpy.ndarray')
    if not isinstance(coordinates_of_interest, np.ndarray):
        print('ERROR (nuc_nuc_link_creation): coordinates_of_interest object should be of type numpy.ndarray')
    if not isinstance(r, numbers.Number):
        print('ERROR (nuc_nuc_link_creation): r object should be numeric')
    if not isinstance(set_angles, np.ndarray):
        print('ERROR (nuc_nuc_link_creation): set_angles object should be of type numpy.ndarray')
    if not isinstance(index, numbers.Number):
        print('ERROR (nuc_nuc_link_creation): r object should be numeric')
    if not isinstance(output, dict):
        print('ERROR (nuc_nuc_link_creation): output object should be of type numpy.ndarray')

    x1 = coordinates_of_interest[0]
    y1 = coordinates_of_interest[1]

    i = 0
    set_of_all_nuc = copy.deepcopy(set_of_all_nuc)

    # note that for full slides, this number may be exceeded
    set_of_all_nuc[index, 0] = 100000000000
    set_of_all_nuc[index, 1] = 100000000000

    # distance between nuclei in the x direction
    a = set_of_all_nuc[:, [0]] - x1
    # disctance between nuclei in the y direction
    b = set_of_all_nuc[:, [1]] - y1

    # angle between nuclei for use in the sectioned unit circle approach being used
    ang = np.sin(a)/np.cos(b)

    # distance between nuclei (includes the x and y components)
    dist = np.sqrt(np.square(a) + np.square(b))
    # keeping only nuclei of lesser distance than the threshold
    keep_dex = np.array([np.where(dist <= r)[0]]).T
    dims = keep_dex.shape[0]

    nucs = np.zeros([dims, 3])  # creating a zero array of proper dimension
    # selects the distances within the threshold as specified by keep_dex
    dist = dist[keep_dex, 0]
    # selects the angles between the nuclei that comply with the distance threshold
    ang = ang[keep_dex, 0]

    nucs[:, [0]] += keep_dex

    nucs[:, [1]] += ang

    nucs[:, [2]] += dist

    i = 0
    for angle in nucs[:, 1]:  # iterates over all angle values in the nucs dictionary

        # iterates over all angle indices in the set_angles list except for the last one
        for dex in range(len(set_angles)-1):
            # will checks for the second last angle position in set_angles
            if dex == (len(set_angles)-2):

                # checks if angle is in the last angular section [6.02138592, 6.28318531]
                if set_angles[dex] <= angle <= set_angles[dex+1]:

                    # if angle section has values NOT already in it
                    if (set_angles[dex], set_angles[dex+1]) not in output:
                        output[(set_angles[dex], set_angles[dex+1])
                               ] = nucs[[i], :]
                    else:  # if angle section has values already in it
                        np.vstack(
                            [output[(set_angles[dex], set_angles[dex+1])], nucs[[i], :]])
            else:

                # for all angular sections except the last one
                if set_angles[dex] <= angle < set_angles[dex + 1]:
                    if (set_angles[dex], set_angles[dex+1]) not in output:
                        output[(set_angles[dex], set_angles[dex+1])
                               ] = nucs[[i], :]
                    else:
                        np.vstack(
                            [output[(set_angles[dex], set_angles[dex+1])], nucs[[i], :]])
        i += 1
    final_dexs = []
    final_vals = []
    for key in output:
        # gets the index of the minimum distance among nuclei for each angular section
        ind = np.argmin(output[key][:, 2])
        # adds this index to the index list
        final_dexs.append(output[key][ind, 0])
        # adds the value associated with this index to the  value list
        final_vals.append(output[key][ind, 2])
    # ensures that all indexes are integer values
    final_dexs = np.array(final_dexs).astype(int)
    final_vals = np.array(final_vals)

    return final_dexs, final_vals