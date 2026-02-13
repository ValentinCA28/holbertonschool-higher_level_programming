#!/usr/bin/python3
""" My class module
"""


class MyClass:
    """ My class
    """

    def __init__(self, name):
        """  Init  .

        Args:
            name (type): Description of name.
        """
        self.name = name
        self.number = 0

    def __str__(self):
        """  Str  .
        """
        return "[MyClass] {} - {:d}".format(self.name, self.number)
