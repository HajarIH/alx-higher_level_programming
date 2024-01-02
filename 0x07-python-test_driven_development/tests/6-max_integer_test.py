#!/usr/bin/python3
"""Unittest for max_integer([])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([]), None)

    def test_no_args(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer(), None)

    def test_1(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([10]), 10)

    def test_2(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([10, 10, 10, 10]), 10)

    def test_3(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([10, 8, 6, 4]), 10)

    def test_4(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([7, 8, 9, 10]), 10)

    def test_5(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([7, 8, 9, 10, 15, 2, 6, 20]), 20)

    def test_6(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([-7, -8, -9, -10, -15, -2, -6, -20, -33, -77, -12, -11, -43]), -2)

    def test_7(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([-7, 8, -9, 10, -15, -2, 6, -20, 33, -77, -12, 11, -43]), 33)

    def test_8(self):
        """Unittest for max_integer([])"""
        self.assertEqual(max_integer([7.567, 8.01, 9.7538, 10.963790, 15.75428, 2.0975, 6.35790, 20.678]), 20.678)
    
    def test_9(self):
        """Unittest for max_integer([])"""
        with self.assertRaises(TypeError):
            max_integer([[3], [4, 8], 16, "Hello"])

    def test_10(self):
        """Unittest for max_integer([])"""
        with self.assertRaises(TypeError):
            max_integer([16, "Hello"])

    def test_11(self):
        """Unittest for max_integer([])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_13(self):
        """Unittest for max_integer([])"""
        with self.assertRaises(TypeError):
            max_integer(10)

    def test_14(self):
        """Unittest for max_integer([])"""
        with self.assertRaises(TypeError):
            max_integer(10.13)

    if __name__ == "__main__":
        unittest.main()
