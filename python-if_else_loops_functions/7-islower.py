#!/usr/bin/python3
def islower(c):
    """Check if a character is lowercase.

    Args:
        c (str): The character to check.

    Returns:
        bool: True if c is lowercase, False otherwise.
    """
    return 97 <= ord(c) <= 122
