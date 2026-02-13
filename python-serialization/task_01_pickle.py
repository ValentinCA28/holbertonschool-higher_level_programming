#!/usr/bin/env python3
"""Module that defines functions and classes."""


import pickle


class CustomObject:

    def __init__(self, name, age, is_student=True):
        """  Init  .

        Args:
            name (type): Description of name.
            age (type): Description of age.
            is_student (type): Description of is_student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display.
        """
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """Serialize.

        Args:
            filename (type): Description of filename.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize.

        Args:
            cls (type): Description of cls.
            filename (type): Description of filename.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.UnpicklingError, OSError, EOFError):
            return None
