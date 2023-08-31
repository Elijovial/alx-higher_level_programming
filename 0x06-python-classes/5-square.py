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

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
