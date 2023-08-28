#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for items in my_list:
            if i < x:
                print(items, end='')
                i += 1
            else:
                break
    except Exception as err:
        pass
    print()
    return i
