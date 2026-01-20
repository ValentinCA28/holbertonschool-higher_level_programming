#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key: The key to add or update.
        value: The value to set for the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
