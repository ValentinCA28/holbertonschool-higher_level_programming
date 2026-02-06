#!/usr/bin/python3
"""Module for Dragon class demonstrating multiple inheritance."""


class SwimMixin:
    """Mixin class providing swimming capability."""

    def swim(self):
        """Perform swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability."""

    def fly(self):
        """Perform flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swimming and flying capabilities."""

    def roar(self):
        """Perform roaring action."""
        print("The dragon roars!")
