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

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The value to assign to the size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """

        # Use the setters of width and
        # height to assign the value to both attributes
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute.

        Args:
            args (tuple): A tuple of arguments to assign to the attributes.
            kwargs (dict): A dictionary of
key/value arguments to assign to the attributes.
        """

        # Define a list of attribute names in the same order as the arguments
        attributes = ["id", "size", "x", "y"]
        # Use a loop to iterate over the arguments and the attribute names
        for i, arg in enumerate(args):
            # Use setattr to assign the argument value to the attribute name
            setattr(self, attributes[i], arg)
        # If args is empty or does not exist, use kwargs instead
        if not args:
            # Use a loop to iterate over the key/value pairs in kwargs
            for key, value in kwargs.items():
                # Use setattr to assign the value to the attribute name
                setattr(self, key, value)
