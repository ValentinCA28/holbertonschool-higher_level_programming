#!/usr/bin/python3
"""Module for adding unique integers from a list."""


def uniq_add(my_list=[]):
    """
    Add all unique integers in a list.

    Args:
        my_list: A list of integers.

    Returns:
        The sum of all unique integers in the list.
    """
    return sum(set(my_list))
