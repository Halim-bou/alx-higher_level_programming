#!/usr/bin/python3
"""
IO functions
"""


def append_write(filename="", text=""):
    """append a text to file and created if it doesn't exist"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
