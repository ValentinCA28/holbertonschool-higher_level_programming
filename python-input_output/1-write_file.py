#!/usr/bin/python3
"""Module that defines functions and classes."""


def write_file(filename="", text=""):
    """Function description.

    Args:
        filename: Description of filename.
        text: Description of text.

    Returns:
        Return value description.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
