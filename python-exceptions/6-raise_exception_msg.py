#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raises a NameError exception with a message.

    Args:
        message (str): The message to include in the exception.

    Raises:
        NameError: Always raises this exception with the provided message.
    """
    raise NameError(message)
