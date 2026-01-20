#!/usr/bin/python3
"""Module to print list integers in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order.

    Args:
        my_list: The list of integers to print in reverse.
    """
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
