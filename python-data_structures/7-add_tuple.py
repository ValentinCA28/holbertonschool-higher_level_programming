#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise.

    Args:
        tuple_a: First tuple (default: empty tuple)
        tuple_b: Second tuple (default: empty tuple)

    Returns:
        A tuple with 2 elements:
        - First element: sum of first elements of tuple_a and tuple_b
        - Second element: sum of second elements of tuple_a and tuple_b
        If a tuple has fewer than 2 elements, 0 is used for missing values
    """
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (a1 + b1, a2 + b2)
