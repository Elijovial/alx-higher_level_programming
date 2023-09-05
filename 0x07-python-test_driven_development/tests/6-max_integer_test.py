#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_max_integer_empty_list(self):
        """Test max_integer with an empty list"""
        actual = max_integer([])
        expected = None
        self.assertEqual(actual, expected)

    def test_max_integer_one_element(self):
        """Test max_integer with a list of one element"""
        actual = max_integer([42])
        expected = 42
        self.assertEqual(actual, expected)

    def test_max_integer_positive_numbers(self):
        """Test max_integer with a list of positive numbers"""
        actual = max_integer([1, 2, 3])
        expected = 3
        self.assertEqual(actual, expected)

    def test_max_integer_negative_numbers(self):
        """Test max_integer with a list of negative numbers"""
        actual = max_integer([-1, -2, -3])
        expected = -1
        self.assertEqual(actual, expected)

    def test_max_integer_mixed_numbers(self):
        """Test max_integer with a list of mixed numbers"""
        actual = max_integer([1, -2, 3])
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
