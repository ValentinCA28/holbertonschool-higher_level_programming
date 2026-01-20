#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set.

    Args:
        set_1: First set.
        set_2: Second set.

    Returns:
        A set containing elements that are in set_1 or set_2 but not in both.
    """
    return set_1 ^ set_2
