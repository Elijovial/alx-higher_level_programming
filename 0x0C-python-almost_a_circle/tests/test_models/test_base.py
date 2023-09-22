#!/usr/bin/python3

# tests/test_models/test_base.py

# Import the unittest module
import unittest
# Import the Base class from models/base.py
from models.base import Base


# Create a test class that inherits from unittest.TestCase
class TestBase(unittest.TestCase):
    """A test class for the Base class."""

    # Define a setUp method that runs before each test
    def setUp(self):
        """Set up an instance of Base for testing."""
        self.base = Base()

    # Define a tearDown method that runs after each test
    def tearDown(self):
        """Clean up the instance of Base after testing."""
        del self.base

    # Define a test method for each task
    # Use the assert methods to check if
    # the expected output matches the actual output
    # Use the docstring to describe what the test method does

    def test_id(self):
        """Test if the id attribute is assigned correctly."""
        # Check if the id of the base instance is 1
        self.assertEqual(self.base.id, 1)
        # Create another instance of Base and check if its id is 2
        base2 = Base()
        self.assertEqual(base2.id, 2)
        # Create another instance of Base with a custom id and check if
        # its id matches the custom id
        base3 = Base(12)
        self.assertEqual(base3.id, 12)

    # Add more test methods as needed


# Add an entry point to execute the tests
# from the command line using unittest.main()
if __name__ == "__main__":
    unittest.main()
