#!/usr/bin/python3
def print_last_digit(number):
    number = abs(number)
    last_number = number % 10
    print(last_number, end="")
