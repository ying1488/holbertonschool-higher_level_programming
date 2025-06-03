#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """ Append to a file
    Returns the number of characters added
    Args: file name (string) and text(string)
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
