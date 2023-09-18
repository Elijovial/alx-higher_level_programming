#!/usr/bin/python3
"""A class module base"""


class Base:
    """A base class for other classes in the project."""

    # A private class attribute to count the number of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): The id of the instance. If None, assign a new id based on __nb_objects.
        """

        # If id is not None, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # Otherwise, increment __nb_objects and assign the new value to id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
