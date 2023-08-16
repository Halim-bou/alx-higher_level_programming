#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set()
    result = 0
    for i in my_list:
        if i not in uniq_num:
            uniq_num.add(i)
            result += i
    return result
