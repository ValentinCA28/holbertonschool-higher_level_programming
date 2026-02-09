#!/usr/bin/python3
"""Module for reading and printing file contents."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: The path to the file to read. Defaults to empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
