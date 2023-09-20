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

    def area(self):
        """Return the area value of the Rectangle instance."""

        # The area of a rectangle is the product of its width and height
        return self.__width * self.__height

    def display(self):
        """Print in stdout the Rectangle instance with the character #."""

        # Print y new lines before the rectangle
        for i in range(self.y):
            print()

        # Use a nested loop to print the rows and columns of the rectangle
        for i in range(self.__height):
            # Print x spaces before each row
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

            # Print a new line after each row
    def __str__(self):
        """Method that override str method
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute.

        Args:
            args (tuple): A tuple of arguments to assign to the attributes.
        kwargs (dict): A dictionary of
key/value arguments to assign to the attributes.
        """

        # Define a list of attribute names in the same order as the arguments
        attributes = ["id", "width", "height", "x", "y"]
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

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""

        # Create a new dictionary with the attributes of the instance
        dictionary = {}
        # Use a loop to iterate over the attribute names
        for attribute in ["id", "width", "height", "x", "y"]:
            # Use getattr to get the value
            # of each attribute and assign it to the dictionary
            dictionary[attribute] = getattr(self, attribute)
        # Return the dictionary
        return dictionary
