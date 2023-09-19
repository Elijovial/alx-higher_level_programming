#!/usr/bin/python3
"""A class module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal offset of the rectangle. Defaults to 0.
            y (int): The vertical offset of the rectangle. Defaults to 0.
            id (int): The id of the rectangle.
            If None, assign a new id based on Base. Defaults to None.
        """

        # Call the super class with id
        super().__init__(id)
        # Assign each argument to the right attribute using setters
        try:
            self.width = width
            self.height = height
            self.x = x
            self.y = y
        # If any exception occurs, re-raise it with the same message
        except Exception as e:
            raise e

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The value to assign to the width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        # Validate the value type and range
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        # Assign the value to the private attribute
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The value to assign to the height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        # Validate the value type and range
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        # Assign the value to the private attribute
        self.__height = value

    @property
    def x(self):
        """Get the x offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x offset of the rectangle.

        Args:
            value (int): The value to assign to x.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        # Validate the value type and range
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        # Assign the value to the private attribute
        self.__x = value

    @property
    def y(self):
        """Get the y offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y offset of the rectangle.

        Args:
            value (int): The value to assign to y.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        # Validate the value type and range
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        # Assign the value to the private attribute
        self.__y = value
