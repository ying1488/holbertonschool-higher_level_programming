#!/usr/bin/python3
"""
Write a class Square that defines a square
"""


class Square:

    """
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
    that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
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

    def my_print(self):
        """
         prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
