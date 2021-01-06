#!/usr/bin/python3
"""Module class definition"""


class Square():
    """Class that defines a Square"""
    def __init__(self, size=0):
        """Inits a square with a given size

        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size
