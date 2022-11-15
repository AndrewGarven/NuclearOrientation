import math
import numpy as np
import numbers


def upper_lower(x1, min_orientation):
    """
    This function determines the upper and lower angular thresholds for a particular
    nuclei (centroid) when determining its nearest neighbors on the basis of orientation.
    Given how visopharm provides angles relative to the horizontal axis and the axial
    definition of angle in this study, it must be noted that the maximum positive/neg
    angular difference that can be observed is of the order pi/2.

    input: x1- angle of nuclei of interest | a- array of form [['(A, 01)' 'x' 'y' 'angle'],...,]
    output: upper- float, upper angle threshold, lower- float, lower angle threshold,
        u_neg- float, upper-negative quadrant threshold | l_pos- float, lower postive quadrant threshold
    """
    if not isinstance(x1, np.ndarray):
        print('ERROR (upper_lower): x1 object should be of type numpy.ndarray')
    if not isinstance(min_orientation, numbers.Number):
        print('ERROR (upper_lower): min_orientation object should be a numeric value')

    NinetyDegrees = math.pi / 2

    upper = []
    lower = []

    if NinetyDegrees >= (x1 + min_orientation):
        # if the upper limit of the acceptable angular difference range is below pi/2
        upper.append([x1 + min_orientation, None])
    else:
        # if the upper limit acceptable angular difference range is above pi/2
        upper.append([NinetyDegrees, -NinetyDegrees + (min_orientation - (NinetyDegrees - x1))])

    if (x1 - min_orientation) >= -NinetyDegrees:
        # if the lower limit acceptable angular difference range is above -pi/2
        lower.append([x1 - min_orientation, None])
    else:
        # if the lower limit acceptable angular difference range is below -pi/2
        lower.append([-NinetyDegrees, NinetyDegrees - (min_orientation + -NinetyDegrees - x1)])

    return upper[0][0], lower[0][0], upper[0][1], lower[0][1]
