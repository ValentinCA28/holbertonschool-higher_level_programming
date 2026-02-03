#!/usr/bin/bash/python3
"""Module that defines functions and classes."""


class VerboseList(list):

    def append(self, item):
        """Function description.

        Args:
            item: Description of item.

        Returns:
            Return value description.
        """
        super().append(item)
        print("Added [{}] to the list".format(item))

    def remove(self, item):
        """Function description.

        Args:
            item: Description of item.

        Returns:
            Return value description.
        """
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def extend(self, item):
        """Function description.

        Args:
            item: Description of item.

        Returns:
            Return value description.
        """
        items = len(item)
        super().extend(item)
        print("Extended [{}] from the list".format(items))

    def pop(self, index=None):
        """Function description.

        Args:
            index: Description of index.

        Returns:
            Return value description.
        """
        if index is None:
           index = -1
        print("Pop [{}] from the list".format(self[index]))
        pop_item = super().pop(index)
        return pop_item
