#!/usr/bin/python3
"""Module that defines functions and classes."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Function description.

        Args:
            width: Description of width.
            height: Description of height.

        Returns:
            Return value description.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
