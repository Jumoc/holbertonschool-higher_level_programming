#!/usr/bin/python3
"""This is a module definition"""


class BaseGeometry():
    """BaseGeometry class creates base geometry"""
    def area(self):
        """Raises an exception on call"""
        raise Exception("area() is not implemented")
