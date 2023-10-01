#!/usr/bin/python3
"""
TDD
"""


def add_integer(a, b=98):
    """
    return int(a) + int(b)
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
