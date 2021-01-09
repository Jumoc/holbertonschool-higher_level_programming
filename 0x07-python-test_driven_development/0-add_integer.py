#!/usr/bin/python3
"""This is the module description for add_integer"""


def add_integer(a, b=98):
    """Function to add to integers
    Args:
        a: first number
        b: second number"""
    types = (int, float)
    if type(a) not in types:
        raise TypeError("a must be an integer")
    if type(b) not in types:
        raise TypeError("b must be an integer")
    return int(a + b)
