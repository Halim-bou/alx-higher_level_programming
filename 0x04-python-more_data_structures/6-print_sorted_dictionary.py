#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s_dic = list(a_dictionary.keys())
    s_dic.sort()
    for key in s_dic:
        print("{} : {}".format(key, a_dictionary.get(key)))
