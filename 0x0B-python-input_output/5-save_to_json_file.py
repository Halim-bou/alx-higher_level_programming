#!/usr/bin/python3
"""
play with json and io
"""
import json


def save_to_json_file(my_obj, filename):
    """save to a file with json"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
