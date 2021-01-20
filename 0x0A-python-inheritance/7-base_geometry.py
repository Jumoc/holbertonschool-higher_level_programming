"""This is a module definition"""


class BaseGeometry():
    """BaseGeometry class creates base geometry"""
    def area(self):
        """Raises an exception on call"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0:
            raise ValueError("{:s} must be greater than 0".format(name))
