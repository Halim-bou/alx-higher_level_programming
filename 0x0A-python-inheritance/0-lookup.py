#!/usr/bin/python3
"""
Function lookup
"""


def lookup(obj):
    """ func that return a list of attributes and methods"""
    attributes = dir(obj)
    return attributes
