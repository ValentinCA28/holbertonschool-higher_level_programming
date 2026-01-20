#!/usr/bin/python3


def element_at(my_list, idx):
    """Retrieves an element from a list at a given index.

    Args:
        my_list: The list to retrieve the element from.
        idx: The index of the element to retrieve.

    Returns:
        The element at the specified index, or None if the index is
        out of range or negative.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
