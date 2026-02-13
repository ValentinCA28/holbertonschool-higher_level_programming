#!/usr/bin/env python3
"""Module that defines functions and classes."""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):

    """Serialize To Xml.

    Args:
        dictionary (type): Description of dictionary.
        filename (type): Description of filename.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):

    """Deserialize From Xml.

    Args:
        filename (type): Description of filename.
    """
    tree_2 = ET.parse(filename)
    root = tree_2.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
