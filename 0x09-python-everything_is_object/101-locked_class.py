#!/usr/bin/python3
class LockedClass:
    """A class that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name."""

    __slots__ = ["first_name"] # define a list of allowed attributes using __slots__

    def __init__(self):
        pass # no need to initialize anything
