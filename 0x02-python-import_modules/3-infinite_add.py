#!/usr/bin/python3
import sys


def add_numbers(numbers):
    my_sum = 0

    for num in numbers:
        my_sum += int(num)
    return my_sum


if __name__ == "__main__":
    numbers = sys.argv[1:]
    result = add_numbers(numbers)
    print("{}".format(result))
