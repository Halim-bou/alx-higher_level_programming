#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)) == 1:
        print("0 argument.")
    elif len(sys.argv) == 2:
        print("1 argument:", end="\n")
        print("1 : {}".format(sys.argv[1]))
    else:
        print(f"{len(sys.argv) - 1} arguments:", end="\n")
        for i in range(len(sys.argv) - 1):
            print("{} : {}".format(i + 1, sys.argv[i + 1]))
