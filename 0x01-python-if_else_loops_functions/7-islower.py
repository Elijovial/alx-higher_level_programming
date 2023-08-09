#!/usr/bin/python3
def islower(c):
    # Check if c is a single character
    if len(c) != 1:
        return False
    # Get the ASCII code of c
    ascii_code = ord(c)
    # Check if the ASCII code is in the range of lowercase letters
    if ascii_code >= 97 and ascii_code <= 122:
        return True
    else:
        return False
