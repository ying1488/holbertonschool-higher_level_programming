#!/usr/bin/python3
"""Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, size):
        """size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area"""
        return self.__size ** self.__size

    def __str__(self):
        """prints breakdown of area"""
        return "[square] {}/{}".format(self.__size, self.__size)
