#!/usr/bin/python3
"""
Write a class Square that defines a square
"""


class Square:

    """
    Write a class Square that defines a square
    by: (based on 3-square.py)
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2
