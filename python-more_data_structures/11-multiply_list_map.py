#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    """Multiply all elements in a list by a number using map.

    Args:
        my_list: List of integers to multiply.
        number: Number to multiply each element by.

    Returns:
        A new list with all values multiplied by number.
    """
    return list(map(lambda x: x * number, my_list))
