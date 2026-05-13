#!/usr/bin/python3


"""
Module 3-to_json_string

This module provides a function to serialize Python objects to their
JSON string representation.
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON string representation of an object.

    Args:
        my_obj (object): The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.

    Raises:
        TypeError: If the object is not serializable to JSON.
    """
    return json.dumps(my_obj)
