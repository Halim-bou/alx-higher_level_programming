#!/usr/bin/python3
"""
function to add attribute
"""


def add_attribute(obj, attr, value):
    """function that add attribute or raise a type error"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
