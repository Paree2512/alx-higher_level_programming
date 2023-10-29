#!/usr/bin/python3

"""Unittest for max_integer([..])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Unit test class"""

    def test_1(self):
        self.assertEqual(max_integer([2, 3, 5]), 5)

    def test_1c(self):
        self.assertEqual(max_integer([2, 13, 5]), 13)

    def test_1d(self):
        self.assertEqual(max_integer([12, 3, 5]), 12)

    def test_1a(self):
        self.assertEqual(max_integer("Hello"), "o")

    def test_1b(self):
        self.assertEqual(max_integer(), None)

    def test_2(self):
        self.assertEqual(max_integer([]), None)

    def test_3(self):
        self.assertEqual(max_integer([10]), 10)

    def test_4(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_5(self):
        self.assertRaises(TypeError, max_integer, None)
