#!/usr/bin/python3
"""
Task 8
"""
from sys import argv
import requests


if __name__ == "__main__":
    lett = "" if len(argv) == 1 else argv[1]
    value = {"q": lett}

    req = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
