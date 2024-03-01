#!/usr/bin/python3
''' Post email'''
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data=data, method="POST")
    with urllib.request.urlopen(req) as res:
        content = res.read()
        print(content.decode("utf-8"))
