#!/usr/bin/python3
"""
creat a class BaseGeometry
"""


class BaseGeometry:
    """function for the class"""
    def area(self):
        """raise exceptions"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """creat a function that check integer validation"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
