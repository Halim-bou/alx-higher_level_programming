#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    str_tolist = list(roman_string)
    for i in range(len(str_tolist) - 1):
        if str_tolist[i] == 'I':
            if str_tolist[i + 1] == 'V':
                str_tolist[i] = 'IV'
                del str_tolist[i + 1]
            if str_tolist[i + 1] == 'X':
                str_tolist[i] = 'IX'
                del str_tolist[i + 1]
        if str_tolist[i] == 'X':
            if str_tolist[i + 1] == 'L':
                str_tolist[i] = 'XL'
                del str_tolist[i + 1]
            if str_tolist[i + 1] == 'C':
                str_tolist[i] = 'XC'
                del str_tolist[i + 1]
        if str_tolist[i] == 'C':
            if str_tolist[i + 1] == 'D':
                str_tolist[i] = 'CD'
                del str_tolist[i + 1]
            if str_tolist[i + 1] == 'M':
                str_tolist[i] = 'CM'
                del str_tolist[i + 1]
    value_roman = {'M': 1000, 'C': 100, 'D': 500,
            'L': 50, 'X': 10, 'V': 5, 'I': 1,
            'XC': 90, 'XL': 40,'CD': 400,
            'CM': 900, 'IV': 4, 'IX': 9}
    Sum = 0
    for i in range(len(str_tolist)):
            for key in value_roman:
                if str_tolist[i] == key:
                    Sum += value_roman[key]
    return Sum
