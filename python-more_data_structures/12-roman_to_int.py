#!/usr/bin/python3
"""Module for converting Roman numerals to integers."""


def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): A string of Roman numerals.

    Returns:
        int: The integer representation of the Roman numeral.
             Returns 0 if roman_string is None or not a string.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    result = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_map.get(char, 0)
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
