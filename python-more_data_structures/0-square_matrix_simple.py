#!/usr/bin/python3
"""Module that contains the square_matrix_simple function."""


def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers in a matrix.

    Args:
        matrix: A 2-dimensional array of integers.

    Returns:
        A new matrix with the same size where each value is the square
        of the value in the input matrix.
    """
    return [[element ** 2 for element in row] for row in matrix]
