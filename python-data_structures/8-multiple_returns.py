#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character.

    Args:
        sentence: The string to process.

    Returns:
        A tuple containing the length of the sentence and its first character.
        If the sentence is empty, the first character is None.
    """
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)
