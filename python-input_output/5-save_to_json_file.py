#!/usr/bin/python3
"""Module that defines functions and classes."""


import json


def save_to_json_file(my_obj, filename):
    """Function description.

    Args:
        my_obj: Description of my_obj.
        filename: Description of filename.

    Returns:
        Return value description.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
