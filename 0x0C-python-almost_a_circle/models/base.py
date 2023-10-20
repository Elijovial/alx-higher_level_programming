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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """

        # Import the json module
        import json
        # Create a filename based on the class name
        filename = cls.__name__ + ".json"
        # Create an empty list to store the dictionaries
        list_dicts = []
        # Use a loop to iterate over the list of objects
        for obj in list_objs:
            # Use the to_dictionary method
            # to convert each object to a dictionary and append it to the list
            list_dicts.append(obj.to_dictionary())
        # Use the static method to_json_string
        # to convert the list of dictionaries to a JSON string
        json_string = cls.to_json_string(list_dicts)
        # Open the file in write mode
        with open(filename, "w") as file:
            # Write the JSON string to the file
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string.
        """

        # Import the json module
        import json
        # If json_string is None or empty, return an empty list
        if not json_string:
            return []
        # Otherwise, use the json.loads
        # method to convert the JSON string to a list of dictionaries
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            dictionary (dict): A dictionary
of key/value arguments to assign to the attributes.

        Returns:
            Base: An instance of the class that inherits from Base.
        """

        # Create a dummy instance with
        # default values for the mandatory attributes
        # For Rectangle, the mandatory attributes are width and height
        # For Square, the mandatory attribute is size
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        # Use the update method to assign
        # the real values from the dictionary to the dummy instance
        dummy.update(**dictionary)
        # Return the dummy instance
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file.

        Returns:
            list: A list of instances who inherits of Base.
        """

        # Import the json and os modules
        import json
        import os
        # Create a filename based on the class name
        filename = cls.__name__ + ".json"
        # Create an empty list to store the instances
        instances = []
        # Check if the file exists
        if os.path.exists(filename):
            # Open the file in read mode
            with open(filename, "r") as file:
                # Read the JSON string from the file
                json_string = file.read()
                # Use the static method from_json_string to convert the
                # JSON string to a list of dictionaries
                list_dicts = cls.from_json_string(json_string)
                # Use a loop to iterate over the list of dictionaries
                for dictionary in list_dicts:
                    # Use the class method create to create an instance from
                    # each dictionary and append it to the list
                    instances.append(cls.create(**dictionary))
        # Return the list of instances
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances who inherits of Base.
        """

        # Import the csv module
        import csv
        # Create a filename based on the class name
        filename = cls.__name__ + ".csv"
        # Open the file in write mode
        with open(filename, "w", newline="") as file:
            # Create a csv writer object
            writer = csv.writer(file)
            # Use a loop to iterate over the list of objects
            for obj in list_objs:
                # Use the to_dictionary
                # method to convert each object to a dictionary
                dictionary = obj.to_dictionary()
                # Create a list of values from the dictionary
                # For Rectangle, the values are id, width, height, x, y
                # For Square, the values are id, size, x, y
                if cls.__name__ == "Rectangle":
                    values = [dictionary["id"], dictionary["width"], dictionary["height"], dictionary["x"], dictionary["y"]]
                elif cls.__name__ == "Square":
                    values = [dictionary["id"], dictionary["size"], dictionary["x"], dictionary["y"]]
                # Write the values to the file as a row
                writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from a file.

        Returns:
            list: A list of instances who inherits of Base.
        """

        # Import the csv and os modules
        import csv
        import os
        # Create a filename based on the class name
        filename = cls.__name__ + ".csv"
        # Create an empty list to store the instances
        instances = []
        # Check if the file exists
        if os.path.exists(filename):
            # Open the file in read mode
            with open(filename, "r", newline="") as file:
                # Create a csv reader object
                reader = csv.reader(file)
                # Use a loop to iterate over the rows in the file
                for row in reader:
                    # Convert each row to a list of integers
                    values = [int(value) for value in row]
                    # Create a dictionary from the values
                    # For Rectangle, the keys are id, width, height, x, y
                    # For Square, the keys are id, size, x, y
                    if cls.__name__ == "Rectangle":
                        keys = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        keys = ["id", "size", "x", "y"]
                    dictionary = dict(zip(keys, values))
                    # Use the class method create to create an instance
                    # from the dictionary and append it to the list
                    instances.append(cls.create(**dictionary))
        # Return the list of instances
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all the Rectangles and Squares.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.
        """

        # Import the turtle module
        import turtle
        # Create a turtle object
        t = turtle.Turtle()
        # Set the speed of the turtle to 10
        t.speed(10)
        # Use a loop to iterate over the list of rectangles
        for rect in list_rectangles:
            # Set the color of the turtle to red
            t.color("red")
            # Move the turtle to the position of the rectangle
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            # Use a loop to draw the rectangle with four sides
            for i in range(4):
                # If it is an even side,
                # move forward by the width of the rectangle
                if i % 2 == 0:
                    t.forward(rect.width)
                # If it is an odd side,
                # move forward by the height of the rectangle
                else:
                    t.forward(rect.height)
                # Turn left by 90 degrees
                t.left(90)
        # Use a loop to iterate over the list of squares
        for square in list_squares:
            # Set the color of the turtle to blue
            t.color("blue")
            # Move the turtle to the position of the square
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            # Use a loop to draw the square with four sides
            for i in range(4):
                # Move forward by the size of the square
                t.forward(square.size)
                # Turn left by 90 degrees
                t.left(90)
        # Exit turtle when done
        turtle.done()
