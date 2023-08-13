#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string.translate({ord('c' and 'C'): None})
    return new_str
