#!/usr/bin/env python3
"""Module that defines functions and classes."""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize And Save To File.

    Args:
        data (type): Description of data.
        filename (type): Description of filename.
    """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load And Deserialize.

    Args:
        filename (type): Description of filename.
    """
    with open(filename, "r") as f:
        return json.load(f)
