#!/usr/bin/python3
"""Module that defines a function to check if an object is exactly
an instance of a specified class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
