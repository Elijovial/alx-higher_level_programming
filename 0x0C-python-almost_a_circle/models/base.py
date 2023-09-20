#!/usr/bin/python3
"""A class module base"""


class Base:
    """A base class for other classes in the project."""

    # A private class attribute to count the number of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance.

        Args:
            id (int): The id of the instance
            . If None, assign a new id based on __nb_objects.
        """

        # If id is not None, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # Otherwise, increment __nb_objects and assign the new value to id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """

        # Import the json module
        import json
        # If list_dictionaries is None or empty, return the string "[]"
        if not list_dictionaries:
            return "[]"
        # Otherwise, use the json.dumps
        # method to convert the list of dictionaries to a JSON string
        return json.dumps(list_dictionaries)
