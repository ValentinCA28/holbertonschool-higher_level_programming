#!/usr/bin/python3
"""Module that defines functions and classes."""


import json

def load_from_json_file(filename):
    """Load From Json File.

    Args:
        filename (type): Description of filename.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
