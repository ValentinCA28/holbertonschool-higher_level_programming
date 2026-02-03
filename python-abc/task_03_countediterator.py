#!/usr/bin/bash/python3
"""Module that defines functions and classes."""


class CountedIterator:
    def __init__(self, iterable):
        """Function description.

        Args:
            iterable: Description of iterable.

        Returns:
            Return value description.
        """
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Function description.

        Returns:
            Return value description.
        """
        return self

    def __next__(self):
        """Function description.

        Returns:
            Return value description.
        """
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        """Function description.

        Returns:
            Return value description.
        """
        return self._count
