#!/usr/bin/python3
"""
json functions
"""
import json


def from_json_string(my_str):
    """json from string to object"""
    return json.load(my_str)
