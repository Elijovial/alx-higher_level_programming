#!/usr/bin/python3
def raise_exception():
    x = "hello"
    if not isinstance(x, int):
        raise TypeError("Only integers are allowed")
