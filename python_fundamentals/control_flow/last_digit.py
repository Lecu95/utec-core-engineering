#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)

if number < 0:
    last_digit = -(abs(number) % 10)
else:
    last_digit = number % 10

prefix = f"Last digit of {number} is {last_digit} and is"

if last_digit > 5:
    print(f"{prefix} greater than 5")
elif last_digit == 0:
    print(f"{prefix} 0")
else:
    print(f"{prefix} less than 6 and not 0")
