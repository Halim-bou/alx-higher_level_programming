#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if 'a' >= s >= 'z':
            s = chr(ord(s) - ord('a') + ord('A'))
        print("{}".format(str))
        print("")
