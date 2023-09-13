#!/usr/bin/python3
"""Reads a text file (UTF-8)"""


def read_file(filename=""):
    """Print the contents of the file to the stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
