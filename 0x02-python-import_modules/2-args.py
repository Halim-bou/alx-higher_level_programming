#!/usr/bin/python3
import sys
lenght = len(sys.argv) - 1
if lenght == 0:
     print("0 arguments.")
elif lenght == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(lenght))
for i in range(lenght):
    print("{} : {}".format(i + 1, sys.argv[i + 1]))
