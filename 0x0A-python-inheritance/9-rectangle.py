#!/usr/bin/python3
"""
subclass Rectangle for class BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass function"""
    def __init__(self, width, height):

        """define and use integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """information of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
