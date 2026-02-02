#!/usr/bin/python3
"""Module that checks if an object is an instance of a specified class."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a class that inherited
        from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
