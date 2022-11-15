from scipy.spatial import cKDTree
import numpy as np


def find_max_distance(dat):
    """
    This function estimates the average distance between nuclei within a core.

    input: dat - array storing the x,y coordinate data
    output: mean - float estimate of mean distance between nuclei
    """
    columns = dat[:, [0, 1]]
    kdt = cKDTree(columns)
    k = 8  # number of nearest neighbors
    dists, neighs = kdt.query(columns, k+1)
    avg_dists = np.mean(np.mean(dists[:, 1:], axis=1))

    return avg_dists