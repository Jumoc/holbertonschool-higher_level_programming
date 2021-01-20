#!/usr/bin/python3
"""This is a module definition"""


def inherits_from(obj, a_class):
    """MyList class that inherits from class list"""
    print(str(a_class) + " " + str(type(obj)) +  " " + str(issubclass(type(obj), a_class)))
    return isinstance(type(obj), a_class)
