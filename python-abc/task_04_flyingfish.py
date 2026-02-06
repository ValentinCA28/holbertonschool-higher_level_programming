#!/usr/bin/python3
"""
Module for FlyingFish class demonstrating multiple inheritance with ABCs.

This module defines abstract base classes for Fish and Flying behavior,
and implements a FlyingFish class that inherits from both.
"""

from abc import ABC, abstractmethod


class Fish(ABC):
    """
    Abstract base class representing a Fish.

    This class defines the interface for fish-like behavior,
    requiring subclasses to implement swimming and habitat methods.
    """

    @abstractmethod
    def swim(self):
        """
        Abstract method for swimming behavior.

        Must be implemented by subclasses to define how the fish swims.
        """
        pass

    @abstractmethod
    def habitat(self):
        """
        Abstract method for habitat description.

        Must be implemented by subclasses to describe where the fish lives.
        """
        pass


class Bird(ABC):
    """
    Abstract base class representing a Bird.

    This class defines the interface for bird-like behavior,
    requiring subclasses to implement flying and habitat methods.
    """

    @abstractmethod
    def fly(self):
        """
        Abstract method for flying behavior.

        Must be implemented by subclasses to define how the bird flies.
        """
        pass

    @abstractmethod
    def habitat(self):
        """
        Abstract method for habitat description.

        Must be implemented by subclasses to describe where the bird lives.
        """
        pass


class FlyingFish(Fish, Bird):
    """
    Class representing a Flying Fish.

    This class demonstrates multiple inheritance by implementing both
    Fish and Bird abstract base classes, providing unique implementations
    for swimming, flying, and habitat methods.
    """

    def swim(self):
        """
        Implement swimming behavior for FlyingFish.

        Prints a message indicating the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Implement flying behavior for FlyingFish.

        Prints a message indicating the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Implement habitat description for FlyingFish.

        Prints a message describing the flying fish's habitat,
        resolving the method name conflict from multiple inheritance.
        """
        print("The flying fish lives both in water and the sky!")
