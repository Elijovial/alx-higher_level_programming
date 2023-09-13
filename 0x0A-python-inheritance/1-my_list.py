#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """A class that inherits from list and has a print_sorted method"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
