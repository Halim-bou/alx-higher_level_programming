#!/usr/bin/python3
"""define a class rectangle"""


class Rectangle:
    """function of this class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width maust be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rect_string = ""
        for i in range(self.__height):
            rect_string += ("#" * self.__width) + "\n"
        return rect_string[:-1]

    def __repr__(self):
        rect_repr1 = "Rectangle(" + str(self.width)
        rect_repr2 = ", " + str(self.__height)+")"
        return (rect_repr1 + rect_repr2)
