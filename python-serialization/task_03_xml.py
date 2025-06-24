#!/usr/bin/python3
"""Serializing and Deserializing with XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """take a Python dictionary
    and a filename as parameters.
    serialize the dictionary into XML
    and save it to the given filename."""
    root = ET.Element("root")
    for k in dictionary.keys():
        ET.SubElement(root, k).text = dictionary[k]

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """This will take a filename as its parameter,
    read the XML data from that file,
    and return a deserialized Python dictionary."""
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
