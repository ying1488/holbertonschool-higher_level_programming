#!/usr/bin/python3
"""Student to JSON
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retreives a dict representation
        of a Student instance
        """
        return self.__dict__
