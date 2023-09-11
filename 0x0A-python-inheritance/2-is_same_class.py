#!/usr/bin/python3
"""function is_same_class"""


def is_same_class(obj, a_class):
    """function that check if the object is exactly instance of the class"""
    if type(obj) is not a_class:
        return False
    else:
        return True
