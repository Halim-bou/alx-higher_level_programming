#!/usr/bin/python3
def max_integer(my_list=[]):
    bigg = 0
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            if my_list[i] > bigg:
                bigg = my_list[i]
    return bigg
