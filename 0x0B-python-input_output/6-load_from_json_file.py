#!/usr/bin/python3
"""
playing with json and io file
"""
import json


def load_from_json_file(filename):
    """creat an object from json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
