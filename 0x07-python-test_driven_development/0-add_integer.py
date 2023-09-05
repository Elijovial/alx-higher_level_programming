#!/usr/bin/python3
"""
This module contains a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b as an integer.

    Args:
        a (int or float): The first operand.
        b (int or float): The second operand (default 98).

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
