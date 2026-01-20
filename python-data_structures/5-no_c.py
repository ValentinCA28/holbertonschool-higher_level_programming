#!/usr/bin/python3


def no_c(my_string):
    """Remove all characters c and C from a string.

    Args:
        my_string: The input string to process.

    Returns:
        A new string with all 'c' and 'C' characters removed.
    """
    if my_string is None:
        return None
    return "".join(char for char in my_string if char not in "cC")
