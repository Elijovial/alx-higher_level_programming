#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
abs_number_str = str(abs(number))
sign = number_str[0]
last_digit = number_str[-1]
if sign == "-":
    if last_digit == "0":
        last_digit = abs_number_str[-1]
    else:
        last_digit = sign + abs_number_str[-1]
else:
    last_digit = abs_number_str[-1]
print(f"Last digit of {number} is {last_digit} ", end="")
if last_digit > "5":
    print("and is greater than 5")
elif last_digit == "0":
    print("and is zero")
else:
    print("and is less than 6 and not 0")
