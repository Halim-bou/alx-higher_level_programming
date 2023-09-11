#!/usr/bin/python3
"""inheritance classes"""


class MyList(list):
    """function for the class"""
    def print_sorted(self):
        """print a list of integers in sorted"""

        list_sorted = sorted(self)
        print(list_sorted)
