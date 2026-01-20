#!/usr/bin/python3
"""Module for safe_print_list function."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list safely.

    Args:
        my_list: The list to print elements from.
        x: The number of elements to print.

    Returns:
        The actual number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
