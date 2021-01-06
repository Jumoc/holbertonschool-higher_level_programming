#!/usr/bin/python3
"""Module class definition"""


class Square():
    """Class that defines a Square"""
    def __init__(self, size=0):
        """Inits a square with a given size

        Args:
            size (int): size of the square
        """
        self.__size = size

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Args:
            value (int): value of the size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
