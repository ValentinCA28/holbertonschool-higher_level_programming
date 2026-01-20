#!/usr/bin/python3
"""Module for finding common elements in two sets."""


def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A set containing elements that are present in both sets.
    """
    return set_1 & set_2
