#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Shape"""
    @abstractmethod
    
    def area (self):
    """area"""
        return 
    
    def perimeter(self):
    """self"""
        return

class Circle(Shape):
    """
    Dog - subclass of Animal
    return sounds Bark
    """
    def sound(self):
        return "Bark"

class Rectangle(Shape):
    """
    Dog - subclass of Animal
    return sound str Meow
    """
    def sound(self):
        return "Meow"
