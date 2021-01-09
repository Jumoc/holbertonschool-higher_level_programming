#!/usr/bin/python3
"""This is the module description"""


def print_square(size):
    """Function that prints of a given size
    Args:
        first_name: first name
        last_name: last name
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [[print("#", end="") if i < size - 1 else print("#")
        for i in range(size)] for j in range(size)]
