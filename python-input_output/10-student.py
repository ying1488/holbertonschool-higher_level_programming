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

    def to_json(self, attrs=None):
        """ that retrieves a dictionary representation of a Student instance
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        else:
            return self.__dict__
