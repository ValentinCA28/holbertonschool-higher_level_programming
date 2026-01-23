#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        """Test with a list containing one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_all_same_values(self):
        """Test with all elements being the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_with_zero(self):
        """Test with zero in the list"""
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)

    def test_only_zero(self):
        """Test with only zero"""
        self.assertEqual(max_integer([0]), 0)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000, 2000, 3000, 4000]), 4000)

    def test_negative_and_zero(self):
        """Test with negative numbers and zero"""
        self.assertEqual(max_integer([-5, -2, 0, -3]), 0)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)

    def test_default_empty_list(self):
        """Test calling function without arguments"""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
