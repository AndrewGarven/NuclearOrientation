import numpy as np
import copy
import numbers
from Funcs.NucleiCount import find_count
from Funcs.MathOrientDist import math_orient_dist
from Funcs.UpperLower import upper_lower


def make_matrix_orient(data, min_orientation):
    """
    This function creates a matrix based on the min_orientation
    threshold and the relative orientation of the centroid nuclei and
    all others. Note this equation does not consider nearest neighor, it simply
    vectorizes the comparison for all data values.

    input: data- a numpy array-data_structure[slide][:, :] | min_orientation- orientation threshold
    output:matrix - matrix representation of orientation connections between nuclei
    """

    if not isinstance(data, np.ndarray):
        print('ERROR (make_matrix_orient): data object should be of type numpy.ndarray')
    if not isinstance(min_orientation, numbers.Number):
        print('ERROR (make_matrix_orient): min_orientation object should be a numeric value')

    count = find_count(data)
    matrix = np.zeros([count, count])
    i = 0
    j = 1000000000000000000
    columns = data

    for x1 in data:
        columns_x = copy.deepcopy(columns).flatten()
        columns_x[i] = j

        upper, lower, u_neg, l_pos = upper_lower(x1, min_orientation)

        # I will increase to the index of nuclear count
        min_indexs, min_vals = math_orient_dist(
            columns_x, x1, min_orientation, upper, lower, u_neg, l_pos, i, j)
        min_indexs = min_indexs.astype("int")
        matrix[min_indexs, i] = min_vals
        matrix[i, min_indexs] = min_vals
        i += 1

    return matrix
