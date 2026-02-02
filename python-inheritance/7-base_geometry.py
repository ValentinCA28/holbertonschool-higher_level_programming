#!/usr/bin/python3
"""Module that defines functions and classes."""


BaseGeometry = __import__('6-base_geometry').BaseGeometry


def area(self):
    """Function description.

    Returns:
        Return value description.
    """
    raise Exception("area() is not implemented")


def integer_validator(self, name, value):
    """Function description.

    Args:
        name: Description of name.
        value: Description of value.

    Returns:
        Return value description.
    """
    if not isinstance(value, int):
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
