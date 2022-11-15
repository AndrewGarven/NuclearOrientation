import numpy as np
from Funcs.NucleiCount import find_count
from Funcs.NuclearLinkCreation import nuc_nuc_link_creation


def make_matrix_dist(data, min_distance):
    """
    This function creates the matrix for the distance metric, connecting
    nuclei on based on spatial proximity.

    input: data- array of x,y vals: data_structure[slide][:, :]
    | min_distance- float value of 1.5x mean distance between nuclei in core
    output: matrix - array of connections made based on distance between nuclei
    """
    if not isinstance(data, np.ndarray):
        print('ERROR (make_matrix_dist): data object should be of type numpy.ndarray')
    if not isinstance(min_distance, float):
        print('ERROR (make_matrix_dist): min_orientation object should be a float value')

    count = find_count(data)
    # create matrix of size #nuclei x #nuclei
    matrix = np.zeros([count, count])
    i = 0
    diff = np.pi/12  # angle threshold for sectioning the 2pi area surrounding a nuclei
    start = 0.00
    num = 25
    set_angles = np.arange(0, num)*diff+start  # create all sections of 2pi
    columns = data[:, [0, 1]]  # x and y vals
    for point in data:
        output = {}

        min_indexs, min_vals = nuc_nuc_link_creation(
            columns, point, min_distance, set_angles, i, output)
        # create links among nuclei of similar orientation

        matrix[[min_indexs], i] = min_vals
        matrix[i, [min_indexs]] = min_vals
        i += 1

    return matrix
