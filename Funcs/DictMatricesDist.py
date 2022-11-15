from Funcs.MakeMatrixDist import make_matrix_dist


def dict_matrices_dist(data_structure, min_distance, slide):
    """
    This function facilitates the creation of matrices for the distance metric
    using the make_matrix_dis function. This function ensures that all cores
    are of a nuclear count > 300.

    input: data_structure- a dictionary storing the x, y coordinate data | min_distance- float value of 1.5x mean distance between nuclei in core
        | slide - core identity (i.e. (A, 01))
    output:matrix - matrix representation of orientation connections between nuclei
    """

    if not isinstance(data_structure, dict):
        print('ERROR (dict_matrices_dist): data object should be of type dict')
    if not isinstance(min_distance, float):
        print('ERROR (dict_matrices_dist): min_orientation object should be a numeric value')
    if not isinstance(slide, str):
        print('ERROR (dict_matrices_dist): slide object should be of type str')

    l = data_structure[slide].shape[0]

    #if l < 300:
    #    print("ERROR (dict_matrices_dist): length of dist data invalid")
    # to test different sizes
    matrix = make_matrix_dist(data_structure[slide][:, :], min_distance)

    return matrix
