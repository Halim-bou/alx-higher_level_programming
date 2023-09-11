#!/usr/bin/python3
"""
functio inherits_from
"""


def inherits_from(obj, a_class):
    """check if the object is an instance of a class that inherited"""
    if issubclass(obj.__class__, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
