#!/usr/bin/python3
"""
task 1
"""

from sys import argv
import urllib.request


url = argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as resp:
    print(dict(resp.headers).get("X-Request-Id"))
