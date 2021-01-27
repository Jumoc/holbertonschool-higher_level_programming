#!/usr/bin/python3
"""Base module defines a base"""
import json
from os import path


class Base():
    """Class Base, defines base geometry and position"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serializes a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects"""
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            n_list = []
            if list_objs is not None:
                [n_list.append(x.to_dictionary()) for x in list_objs]
            f.write(cls.to_json_string(n_list))

    @staticmethod
    def from_json_string(json_string):
        """Deserializes json into an object"""
        my_list = []
        if json_string is not None:
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """Creates an object from a dictionary"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads object dictionaries from a file"""
        instances_list = []
        if path.exists("{}.json".format(cls.__name__)):
            with open(
                    "{}.json".format(cls.__name__), "r", encoding="utf-8"
                    ) as f:
                new_list = cls.from_json_string(f.read())
                for item in new_list:
                    instances_list.append(cls.create(**item))
        return instances_list
