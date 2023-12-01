#!/usr/bin/python3
"""
task 2
"""

import urllib.parse
import urllib.request
import sys


url = sys.argv[1]
value = {'email': sys.argv[2]}
data = urllib.parse.urlencode(value).encode("ascii")
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as resp:
    print(resp.read().decode("utf-8"))
