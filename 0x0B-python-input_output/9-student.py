#!/usr/bin/python3
"""Module description for Student"""


class Student():
    """Defines a student with names and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """returns the dict of the object"""
        return self.__dict__

