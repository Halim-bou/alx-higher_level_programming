#!/usr/bin/python3
"""define a class square"""


class Square:
    """initialize the square"""
    type_error = "position must be a tuple of 2 positive integers"

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            slef.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError(self.type_error)
        elif len(value) != 2:
            raise TypeError(self.type_error)
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError(self.type_error)
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")
