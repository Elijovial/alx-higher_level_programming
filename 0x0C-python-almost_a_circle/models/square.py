#!/usr/bin/python3
"""A class module square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The horizontal offset of the square. Defaults to 0.
            y (int): The vertical offset of the square. Defaults to 0.
            id (int): The id of the square.
If None, assign a new id based on Base. Defaults to None.
        """

        # Call the super class with id, x, y, width and height
        # The width and height must be assigned to the value of size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square instance."""

        # Use the format method to create a
        # string with the attributes of the instance
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                  self.width))
