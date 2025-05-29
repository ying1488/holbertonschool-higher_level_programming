#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Animal"""

class Animal(ABC):
    """Animal"""
    @abstractmethod
    def sound (self):
        return ""

class Dog(Animal):
    """
    Dog - subclass of Animal
    return sounds Bark
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Dog - subclass of Animal
    return sound str Meow
    """
    def sound(self):
        return "Meow"
