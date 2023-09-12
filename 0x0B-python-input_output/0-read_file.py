#!/usr/bin/python3
"""
function to read a file
"""


def read_file(filename=""):
    """func to read file"""
    with open(filename, encoding="utf-8") as f:
        read_txt = f.read()
        print(read_txt, end='')
