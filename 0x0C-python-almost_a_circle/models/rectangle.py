#!/usr/bin/python3
"""Base module defines a rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle, defines its width, height, x and y"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def _not_integer(self, name, value):
        """Checks if value is not an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def _is_negative(self, name, value):
        """Checks if value is negative"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def _is_zero(self, name, value):
        """Checks if value is negative or zero"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """Getter of attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of attribute width"""
        self._not_integer("width", value)
        self._is_zero("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter of attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of attribute height"""
        self._not_integer("height", value)
        self._is_zero("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter of attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of attribute x"""
        self._not_integer("x", value)
        self._is_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """getter of attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of attribute y"""
        self._not_integer("y", value)
        self._is_negative("y", value)
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """Print to stdout the square with the character #"""
        [print() for i in range(self.y)]
        for i in range(self.height):
            for j in range(self.width + self.x):
                    if j < self.x:
                        print(" ", end="")
                    else:
                        print("#", end="")
            print()

    def __str__(self):
        """Return data about a rectangle"""
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
        return string

    def update(self, *args, **kwargs):
        """Updates the attributes of the current object"""
        attrs = ("id", "width", "height", "x", "y")
        if args is not None and len(args) > 0:
            [self.__setattr__(attrs[i], args[i]) for i in range(len(args))]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if str(key) in attrs:
                        self.__setattr__(key, value)

    def to_dictionary(self):
        """Returns the attributes of the current object"""
        n_dict = {
            "id": self.id, "width": self.width, "height": self.height,
            "x": self.x, "y": self.y
        }
        return n_dict
