#!/usr/bin/env python3
"""Basic Serialization
"""

import json


def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    json_data = json.dumps(data, filename)
    print(json_data)


def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    des_data = filename(**json.loads(filename))
    print(des_data)
