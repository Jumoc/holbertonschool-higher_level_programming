#!/usr/bin/python3
"""This is a module definition"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """BaseGeometry class creates base geometry"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
