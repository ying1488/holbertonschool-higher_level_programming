#!/usr/bin/env python3
"""Pickling Custom Classes
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name},Age: {self.age}, Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
                return (data)
        except (EOFError, pickle.UnpicklingError):
            print("file is damaged")
        return
