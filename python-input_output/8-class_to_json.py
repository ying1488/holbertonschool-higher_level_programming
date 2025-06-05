#!/usr/bin/python3

""" Class to JSON
    a function that returns the dictionary
    description with simple data structure
    of an object
"""

import json


def class_to_json(obj):
    return obj.__dict__
