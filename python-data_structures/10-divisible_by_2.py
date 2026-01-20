#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.

    Args:
        my_list: A list of integers.

    Returns:
        A new list with True or False depending on whether the integer
        at the same position in the original list is a multiple of 2.
    """
    if my_list is None:
        return None

    return [element % 2 == 0 for element in my_list]
