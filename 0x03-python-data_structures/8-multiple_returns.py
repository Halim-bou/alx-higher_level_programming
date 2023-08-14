#!/usr/bin/python3
def multiple_returns(sentence):
    the_tuple = ()
    if len(sentence) == 0:
        the_tuple = 0, "None"
        return the_tuple
    else:
        the_tuple = len(sentence), sentence[0]
        return the_tuple
