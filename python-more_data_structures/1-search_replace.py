#!/usr/bin/python3
"""Module for search and replace function."""


def search_replace(my_list, search, replace):
    """Replace all occurrences of an element in a list with another element.

    Args:
        my_list: The original list to search in.
        search: The element to search for.
        replace: The element to replace search with.

    Returns:
        A new list with all occurrences of search replaced by replace.
    """
    if my_list is None:
        return None
    return [replace if element == search else element for element in my_list]
