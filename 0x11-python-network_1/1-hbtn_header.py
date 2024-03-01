#!/usr/bin/python3
'''fetsh header object'''
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        object = r.headers.get('X-Request-Id')
        print(object)
