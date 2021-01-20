#!/usr/bin/python3
"""This is a module definition for add attribute"""


def add_attribute(obj, attr, value):
    """adds attributes
    Args:
        obj: name of the value
        attr: value to be checked
        value: value"""
    if hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
