#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape"""
    @abstractmethod
    def area(self):
        """area"""
        pass

    def perimeter(self):
        """perimeter"""
        pass


class Circle(Shape):
    """ Circle """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2**3.14

    def perimeter(self):
        return 2*self.radius*3.14


class Rectangle(Shape):
    """ Rectangle """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return (2 * (self.width * self.height))


def shape_info(shape):
    """
    shape info - prints area and perimeter of a shape
    args: shape
    """
    print(f"area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
