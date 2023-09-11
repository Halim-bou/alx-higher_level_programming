#!/usr/bin/python3
"""
function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """return True if object is an instance of a class otherwise return False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
