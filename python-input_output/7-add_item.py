#!/usr/bin/python3
"""
Load, add, save

"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv

filename = "add_item.json"

try:
    """Load, add, save"""
    with open(filename, encoding="utf-8") as f:
        items = json.load(f)
except FileNotFoundError:
    items = []

items.extend(args[1:])

with open(filename, "w", encoding="utf-8") as f:
    json.dump(items, f)
