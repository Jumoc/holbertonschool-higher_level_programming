#!/usr/bin/python3
"""Module class definition"""


class Square():
    """Class that defines a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Inits a square with a given size

        Args:
            size (int): size of the square
            position (tuple) = position of the square

        """
        self.position = position
        self.size = size

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

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square
        Args:
            value (int): value of the position
        """
        if type(value) != tuple or len(value) != 2\
            or type(value[0]) != int or value[0] < 0\
            or type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square filled with this #"""
        if self.size == 0:
            print("")
        else:
            [print() for i in range(self.position[1])]
            for i in range(self.size):
                for j in range(self.size + self.position[0]):
                    if j < self.position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
