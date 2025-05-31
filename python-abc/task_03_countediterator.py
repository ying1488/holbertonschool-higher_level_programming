#!/usr/bin/env python3
""" CountedIterator """


class CountedIterator:
    """ CountedIterator """

    def __init__(self, iterable):
        """
        Initialise CountedIterator with an iterable.
        Args: iterable (obj)
        """
        self.__iter__ = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Returns the CountedIterator object itself to enable iteration
        Returns: The Counted Iteratir object
        """
        return self

    def get_count(self):
        return self.count

    def __next__(self):
        i = next(self.__iter__)
        self.count = self.count + 1
        return i
