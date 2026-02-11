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

    def to_json(self):
        """To Json.
        """
        return self.__dict__
