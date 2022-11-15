import numbers
from Funcs.MakeMatrixOrient import make_matrix_orient


def dict_matrices_orient(data_orient, min_orientation, slide):  # edited
    """
    This function facilitates the creation of matrices for the orientation metric
    using the make_matrix_orient function. This function ensures that all cores
    are of a nuclear count > 300.

    input: data_orient- a dictionary storing the orientation data | min_orientation- orientation threshold
        | slide - core identity (i.e. (A, 01))
    output:matrix - matrix representation of orientation connections between nuclei
    """
    if not isinstance(data_orient, dict):
        print('ERROR (dict_matrices_orient): data object should be of type dict')
    if not isinstance(min_orientation, numbers.Number):
        print('ERROR (dict_matrices_orient): min_orientation object should be a numeric value')
    if not isinstance(slide, str):
        print('ERROR (dict_matrices_orient): slide object should be of type str')

    l = data_orient[slide].shape[0]

    #if l < 300:
    #    print("ERROR (dict_matrices_orient): length of orient data invalid")

    matrix = make_matrix_orient(data_orient[slide][:], min_orientation)

    return matrix