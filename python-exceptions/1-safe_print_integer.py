def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value: The value to print as an integer.

    Returns:
        True if value is an integer and was printed correctly, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
