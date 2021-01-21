#!/usr/bin/python3
"""Module description for class_to_json"""


def class_to_json(obj):
    """returns the json representation of an object"""
    return obj.__dict__
