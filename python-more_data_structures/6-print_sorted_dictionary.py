#!/usr/bin/python3
"""Module for printing sorted dictionary."""


def print_sorted_dictionary(a_dictionary):
    """Print a dictionary with keys in alphabetical order.

    Args:
        a_dictionary: The dictionary to print.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
