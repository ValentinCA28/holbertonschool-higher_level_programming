#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """A base class for geometry operations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises an exception indicating area() is not
                implemented.
        """
        raise Exception("area() is not implemented")
