#!/usr/bin/python3
"""BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle and inherits from BaseGeometry"""

    def __init__(self, width, height):
        """A method that initializes a rectangle with width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
