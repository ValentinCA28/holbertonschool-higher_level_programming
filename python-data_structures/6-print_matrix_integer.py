#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    Args:
        matrix: A list of lists containing integers.

    Returns:
        None
    """
    for row in matrix:
        for j, element in enumerate(row):
            if j > 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print()
