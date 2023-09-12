#!/usr/bin/python3
"""
a multiple inheritance class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """function implemente"""
    def __init__(self, size):
        """define arguments and check inteer validator"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """square operation"""
        return self.__size ** 2
