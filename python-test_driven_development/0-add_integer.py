#!/usr/bin/python3
"""Module for integer addition.

This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float). Defaults to 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
