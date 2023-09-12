#!/usr/bin/python3
"""
func toopen and write in a text file
"""


def write_file(filename="", text=""):
    """write in a file if it doesn't exist creat a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
