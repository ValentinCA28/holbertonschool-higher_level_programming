#!/usr/bin/python3
"""Module that defines functions and classes."""


import json

def load_from_json_file(filename):
    """Function description.

    Args:
        filename: Description of filename.

    Returns:
        Return value description.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
