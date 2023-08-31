#!/usr/bin/python3
"""This module contains a class Square that defines a square."""


class Square:
    """A class Square that defines a square."""
    def __init__(self, size=0):
        """Initializes an instance of the Square class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes the area of the square."""
        return self.__size ** 2
