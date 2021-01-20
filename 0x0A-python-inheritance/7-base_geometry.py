#!/usr/bin/python3
"""This is a module definition for Base geometry
    Class:
        BaseGeometry"""


class BaseGeometry():
    """BaseGeometry class creates base geometry
        for any geometric shape"""
    def area(self):
        """Raises an exception on call to get implemented
            on subclasses"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer
            Args:
                name: name of the value
                value: value to be checked"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
