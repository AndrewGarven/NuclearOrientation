import numpy as np
import numbers


def math_orient_dist(k, x1, min_orientation, upper, lower, u_neg, l_pos, i, j):
    """
    This function determines the upper and lower angular thresholds for a particular
    nuclei (centroid) when determining its nearest neighbors on the basis of orientation.

    input: k- column (array) of orientations | x1 -orientation of nuclei of interest
    | min_orientation- minimum orientation threshold | upper- float, upper angle threshold
    | lower- float, lower angle threshold |u_neg- float, upper-negative quadrant threshold
    | l_pos- float, lower postive quadrant threshold | i- int, index of current nuclei
    | j = int, unique/very large number to set the nuclei's angle apart from others

    output:
    """
    if not isinstance(k, np.ndarray):
        print('ERROR (math_orient_dist): k object should be of type numpy.ndarray')
    if not isinstance(x1, np.ndarray):
        print('ERROR (math_orient_dist): x1 object should be of type numpy.ndarray')
    if not isinstance(min_orientation, numbers.Number):
        print('ERROR (math_orient_dist): min_orientation object should be a numeric value')
    if not isinstance(i, int):
        print('ERROR (math_orient_dist): i object should be a int value')
    if not isinstance(j, int):
        print('ERROR (math_orient_dist): j object should be a int value')

    DexVal = []

    if u_neg == None and l_pos == None:
        # if the range of acceptable angles given the angular threshold is between pi/2 and -pi/2
        dexs = np.array(np.where((upper >= k) & (k >= lower) & (j != k)))
        #dexs = np.delete(dexs, i)

        vals = np.abs(np.abs(k[dexs]) - np.abs(x1)) / min_orientation
        vals = 1 - vals
        DexVal.append([dexs, vals])

    elif l_pos is not None:

        dexs1 = np.array(np.where((upper >= k) & (k >= lower) & (j != k)))
        #dexs1 = np.delete(dexs1, i)
        vals1 = np.abs(np.abs(k[dexs1]) - np.abs(x1)) / min_orientation

        dexs2 = np.array(np.where((k >= l_pos) & (j != k)))
        #dexs2 = np.delete(dexs2, i)
        vals2 = np.abs(min_orientation - (np.pi / 2 - k[dexs2])) / min_orientation

        dexs = np.concatenate((dexs1, dexs2), axis=1)
        vals = np.concatenate((vals1, vals2), axis=1)
        vals = 1 - vals

        DexVal.append([dexs, vals])

    elif u_neg is not None:
        dexs1 = np.array(np.where((upper >= k) & (k >= lower) & (j != k)))
        #dexs1 = np.delete(dexs1, i)
        vals1 = np.abs(np.abs(k[dexs1]) - np.abs(x1)) / min_orientation

        dexs2 = np.array(np.where((u_neg >= k) & (j != k)))
        #dexs2 = np.delete(dexs2, i)
        vals2 = np.abs((np.pi / 2 + k[dexs2]) + min_orientation) / min_orientation

        dexs = np.concatenate((dexs1, dexs2), axis=1)
        vals = np.concatenate((vals1, vals2), axis=1)
        vals = 1 - vals

        DexVal.append([dexs, vals])

    return DexVal[0][0], DexVal[0][1]
