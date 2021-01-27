#!/usr/bin/python3
"""Base module defines a rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square, defines its size, x, y and id"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """getter of attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of attribute size"""
        self.width = value
        self.height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the current instance"""
        attrs = ("id", "size", "x", "y")
        if args is not None and len(args) > 0:
            [self.__setattr__(attrs[i], args[i]) for i in range(len(args))]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if str(key) in attrs:
                        self.__setattr__(key, value)

    def to_dictionary(self):
        """Returns a dictionary with the current instance attributes"""
        n_dict = {
            "id": self.id, "size": self.size,
            "x": self.x, "y": self.y
        }
        return n_dict
