#!/usr/bin/python3
"""Module that defines functions and classes."""


def inherits_from(obj, a_class):
    """Function description.

    Args:
        obj: Description of obj.
        a_class: Description of a_class.

    Returns:
        Return value description.
    """
    return isinstance(obj, a_class) and not isinstance(obj, a_class)
