#!/usr/bin/bash/python3
"""Module that defines functions and classes."""


from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def area(self):
        """Function description.

        Returns:
            Return value description.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Function description.

        Returns:
            Return value description.
        """
        pass


class Circle(Shape):
    def __init__(self, radius):
        """Function description.

        Args:
            radius: Description of radius.

        Returns:
            Return value description.
        """
        self.radius = radius

    def area(self):
        """Function description.

        Returns:
            Return value description.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Function description.

        Returns:
            Return value description.
        """
        return math.pi * (2 * self.radius)


class Rectangle(Shape):
    def __init__(self, width, height):
        """Function description.

        Args:
            width: Description of width.
            height: Description of height.

        Returns:
            Return value description.
        """
        self.width = width
        self.height = height

    def area(self):
        """Function description.

        Returns:
            Return value description.
        """
        return self.height * self.width

    def perimeter(self):
        """Function description.

        Returns:
            Return value description.
        """
        return (self.height + self.width) * 2


def shape_info(shape):
    """Function description.

    Args:
        shape: Description of shape.

    Returns:
        Return value description.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
