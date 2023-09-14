#!/usr/bin/python3
"""Write a function"""


def inherits_from(obj, a_class):
    """A function that checks if an object
    is an instance of a subclass of a class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
