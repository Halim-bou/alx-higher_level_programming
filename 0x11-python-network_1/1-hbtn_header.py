#!/usr/bin/python3
"""
task 1
"""

import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as resp:
    print(dict(resp.headers).get("X-Request-Id"))
