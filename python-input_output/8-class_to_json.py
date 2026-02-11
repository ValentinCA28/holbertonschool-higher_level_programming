#!/usr/bin/python3
"""Serialize class instances into JSON-friendly dictionaries."""


def class_to_json(obj):
    """Return a dictionary description of a simple object for JSON.

    Args:
            obj: The object to serialize.

    Returns:
            dict: The object's attribute dictionary.

    Raises:
            TypeError: If the object cannot be serialized via ``__dict__``.
    """
    if obj is None or not hasattr(obj, "__dict__"):
        raise TypeError("Object is not JSON serializable")

    return dict(obj.__dict__)
