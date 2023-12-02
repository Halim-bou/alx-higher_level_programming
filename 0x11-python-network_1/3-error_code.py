#!/usr/bin/python3
"""
Task 3
"""
import sys
import urllib.request
import urllib.error


if _name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as req:
            print(req.read().decode("utf-8"))
    except error.HTTPError as err:
        print('Error code:', err.code)
