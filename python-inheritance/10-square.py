#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square.

    Inherits from Rectangle class.
    """

    def __init__(self, size):
        """Initializes a square.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
