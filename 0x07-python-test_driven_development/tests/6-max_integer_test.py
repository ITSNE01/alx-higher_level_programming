#!/usr/bin/python3
"""Unittests for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max integer is at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 3.5, 2.1, 7.8]), 7.8)

    def test_mixed_list(self):
        """Test a list of mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.7]), 4.7)

    def test_identical_elements(self):
        """Test a list with all identical elements."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -7]), -1)

    def test_mixed_signs(self):
        """Test a list with mixed positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 5, 3, -4]), 5)

if __name__ == '__main__':
    unittest.main()
