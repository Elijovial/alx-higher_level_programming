#!/usr/bin/python3
"""Write a string to a text file"""


def write_file(filename="", text=""):
    """return the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        f.read()
        return f.tell()
