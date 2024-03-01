#!/usr/bin/python3
import urllib.request
from sys import argv

url = argv[1]
with urllib.request.urlopen(url) as r:
    object = r.headers.get('X-Request-Id')
    print(object)
