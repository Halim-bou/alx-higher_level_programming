#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if 'a' >= s <= 'z':
            s = chr(ord(s) - 32)
        print("{}".format(str), end="")
    print("")
