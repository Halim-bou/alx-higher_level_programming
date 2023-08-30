#!/usr/bin/python3
"""define a class square"""


class Square:
    """initialize a new size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """public instance method that return a square"""
    def area(self):
        return self.__size * self.__size
