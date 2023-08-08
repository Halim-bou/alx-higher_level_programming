#!/usr/bin/python3
import random
number = random.randint(-1000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater then 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less tha 6 and not 0")
