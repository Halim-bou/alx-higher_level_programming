#!/usr/bin/python3
"""
task1
"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as ur:
    content = ur.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
