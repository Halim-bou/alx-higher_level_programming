#!/usr/bin/python3
s = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - s)), end="")
    s = 32 if s == 0 else 0
