#!/usr/bin/python3
"""define a class square"""


class Square:
    """initialixe a new square"""
    def __init__(self, size=0):
        self.__size = size

        """attribute property"""
    @property
    def size(self):
        return self.__size

    """attribute property setter to set it"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

        """public method that return the square """
    def area(self):
        return self.__size * self.__size

    """public instance method that print '#' square"""
    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
