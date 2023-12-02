#!/usr/bin/python3
"""
Task 7
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
