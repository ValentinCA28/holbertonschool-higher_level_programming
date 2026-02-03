#!/user/bin/bash/python3
"""Module that defines functions and classes."""


from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        """Function description.

        Returns:
            Return value description.
        """
        pass


class Dog(Animal):
    def sound(self):
        """Function description.

        Returns:
            Return value description.
        """
        return ("Bark")


class Cat(Animal):
    def sound(self):
        """Function description.

        Returns:
            Return value description.
        """
        return ("Meow")
