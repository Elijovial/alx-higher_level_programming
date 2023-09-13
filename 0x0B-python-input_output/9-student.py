#!/usr/bin/python3
""" Class module"""


class Student:
    """Defines a student by first name, last name and age"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student instance with public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a student instance"""
        return self.__dict__
