#!/usr/bin/python3
"""Module description for Student"""


class Student():
    """Defines a student with names and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dict of the object"""
        if type(attrs) != list:
            return self.__dict__
        else:
            n_dict = {}
            for att in attrs:
                value = self.__dict__.get(att)
                if value is not None:
                    n_dict[att] = value
        return n_dict

    def reload_from_json(self, json):
        """returns the dict of the object"""
        self.__dict__.clear()
        self.__dict__ = json.copy()
