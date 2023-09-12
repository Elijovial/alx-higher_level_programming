#!/usr/bin/python3
def write_file(filename="", text=""):

    """Writes a string to a text file and returns the number of characters written"""

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        f.read()
        return f.tell()
