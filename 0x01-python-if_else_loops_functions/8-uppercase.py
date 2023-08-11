#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            #subtract 32 to get the corresponding uppercase
            c = chr(ord(c) - 32)
            print("{}".format(c), end="" if c == "" else "\n")
            print(end="" if c == "" else "\n")
