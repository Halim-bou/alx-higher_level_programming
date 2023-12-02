#!/usr/bin/python3
"""
Task 9
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main_-":
    author = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=author)
    print(req.json().get("id"))
