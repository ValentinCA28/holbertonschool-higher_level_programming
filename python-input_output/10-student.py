#!/usr/bin/python3
"""Module that defines functions and classes."""


class Student:

    def __init__(self, first_name, last_name, age):
        """  Init  .

        Args:
            first_name (type): Description of first_name.
            last_name (type): Description of last_name.
            age (type): Description of age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To Json.

        Args:
            attrs (type): Description of attrs.
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict
