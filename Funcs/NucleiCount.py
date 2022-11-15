import numpy as np


def find_count(matrix):
    """
    This function returns the number of nuclei in a given
    core when converted to matrix form.

    input: matrix- a matrix
    ouput: count - number of nuclei
    """
    if not isinstance(matrix, np.ndarray):
        print('ERROR (find_count): row object should be of type numpy.ndarray')

    count, c = matrix.shape
    return count