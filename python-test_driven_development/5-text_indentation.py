#!/usr/bin/python3
"""Module for text indentation.

This module provides a function text_indentation(text) that
prints a text, adding 2 new lines after each of these characters:
'.', '?' and ':'.
"""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The string to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # Skip leading spaces at the beginning of a line
        while i < len(text) and text[i] == ' ':
            i += 1

        # Print characters until we hit punctuation or end
        while i < len(text):
            print(text[i], end="")
            if text[i] in '.?:':
                print("\n\n", end="")
                i += 1
                break
            i += 1
