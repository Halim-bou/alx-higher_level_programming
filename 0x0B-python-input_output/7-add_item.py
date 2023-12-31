#!/usr/bin/python3
"""
io and json
"""
import sys
import json
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if os.path.isfile(filename):
    filelist = load_from_json_file(filename)
else:
    filelist = []
i = 0
for item in sys.argv:
    if i != 0:
        filelist.append(item)
    i += 1
save_to_json_file(filelist, filename)
