#!/usr/bin/python3
"""This is a module definition"""


def inherits_from(obj, a_class):
    """MyList class that inherits from class list"""
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
