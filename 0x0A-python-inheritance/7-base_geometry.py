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
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
