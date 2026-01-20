#!/usr/bin/python3
"""Module that deletes an item at a specific position in a list."""


def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list.

    Args:
        my_list: The list to delete from
        idx: The index position to delete at

    Returns:
        The same list with the item deleted, or unchanged if idx is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
