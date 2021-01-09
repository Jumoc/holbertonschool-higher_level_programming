#!/usr/bin/python3
"""This is the module description"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>
    Args:
        first_name: first name
        last_name: last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
