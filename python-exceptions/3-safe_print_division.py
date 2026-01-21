#!/usr/bin/python3
"""Module for safe division operations."""


def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a: The dividend (numerator).
        b: The divisor (denominator).

    Returns:
        The result of the division, or None if division by zero occurs.
    """
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
