#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv)) == 1:
        print("0 argument.")
    elif len(argv) == 2:
        print("1 argument:", end="\n")
        print("1 : {}".format(argv[1]), end="\n")
    else:
        print(f"{len(argv) - 1} arguments:", end="\n")
        for i in range(len(argv) - 1):
            print("{} : {}".format(i + 1, argv[i + 1]))
