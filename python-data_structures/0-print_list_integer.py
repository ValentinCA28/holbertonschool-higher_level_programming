#!/usr/bin/python3
"""Module that contains the print_list_integer function."""


def print_list_integer(my_list=[]):
    """Print all integers of a list.

    Args:
        my_list: The list of integers to print.
    """
    for i in my_list:
        print("{:d}".format(i))
