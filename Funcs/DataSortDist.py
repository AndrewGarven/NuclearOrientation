import numpy as np


def data_sort_dist(row, data_structure):  # data_structure
    """
    This function takes row from the numpy array, a, and organizes it
    into the data_structure dictionary, eliminating a visopharm bug present
    in the index 0 position of some rows where the length of the index 0 value
    is far longer than it should be and, hence, needs to be eliminated
    This function makes the dictionary that will be used for distance calculations.

    input:row-a list in array "a" | data_structure-dictionary with key value
        of (slide letter, #), storing x,y and angle values

    output: na- just adds to data_structure
    """
    if not isinstance(row, np.ndarray):
        print('ERROR (data_sort_dist): row object should be of type numpy.ndarray')
    if not isinstance(data_structure, dict):
        print('ERROR (data_sort_dist): data_structure object should be of type dict')

    if row[0] not in data_structure and (9 >= len(row[0])):
        corr = row[1:].astype("float")
        data_structure[row[0]] = corr

    elif 9 >= len(row[0]):
        corr = row[1:].astype("float")
        data_structure[row[0]] = np.vstack([data_structure[row[0]], corr])

    return data_structure
