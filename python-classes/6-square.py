#!/usr/bin/python3
"""
Write a class Square that defines a square
"""


class Square:

    """
    Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value):
    Private instance attribute: position:
    property def position(self): to retrieve it
    property setter def position(self, value): to set it:
    Instantiation with optional size and optional position:
    def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
    that prints in stdout the square with the character #:
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
         prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
            return
        # vertical
        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            print(" " * self.position[0] + '#' * self.size)
