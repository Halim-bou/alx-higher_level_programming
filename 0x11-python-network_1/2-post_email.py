#!/usr/bin/python3
"""
task 2
"""

import urllib.parse
import urllib.request
from sys import argv


url = argv[1]
value = {'email': argv[2]}
data = urllib.parse.urlencode(value).encode("ascii")
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as resp:
    print(resp.read().decode("utf-8"))
