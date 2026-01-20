#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list.

    Args:
        my_list: A list that may contain any type of elements.

    Returns:
        The sum of all unique integers in the list.
    """
    unique_ints = set()
    for element in my_list:
        try:
            unique_ints.add(element)
        except (ValueError, TypeError):
            continue
    return sum(unique_ints)
