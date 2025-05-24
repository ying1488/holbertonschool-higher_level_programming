#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by:
"""


class Rectangle:
    """
    Private instance attribute: width:
    property def width(self): to retrieve it
    property setter def width(self, value):

    Private instance attribute: height:
    property def height(self): to retrieve it
    property setter def height(self, value): to set it:

    Instantiation with optional width and height:
    def __init__(self, width=0, height=0):

    Public instance method:
    def perimeter(self):
        that returns the rectangle perimeter:
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the current rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the current rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)

        lines = []
        for i in range(self.height):
            line = symbol * self.width
            lines.append(line)
        rectangle_string = "\n".join(lines)
        return rectangle_string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
