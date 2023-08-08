#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
print(f"Last digit of {number} is {number_str[-1:]}", end="")
if number_str[-1:] > "5":
    print(" and is greater than 5\n")
elif number_str[-1:] == "0":
    print(" and is zero\n")
else:
    print(" and is less than 6 and not 0\n")

