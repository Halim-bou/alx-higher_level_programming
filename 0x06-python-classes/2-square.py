#!/usr/bin/python3
"""define a class square"""


class Square:
    """initialize a new square"""
    def __init__(self, size=0):
        """private instance attribute size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
