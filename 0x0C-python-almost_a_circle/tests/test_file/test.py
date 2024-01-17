#!/usr/bin/python3
"""model for tests"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test(unittest.TestCase):
    """test the Base class"""
    def test_1(self):
        """instantiate class"""
        Base._Base_nb_objects = 0
        pass

    def test_2(self):
        """cleans up after each test"""
        pass

    def test_3(self):
        """test if nb_object is private"""
        self.assertTrue(hasattr(Base, "_Base_nb_objects"))

    def test_4(self):
        """test if _nb_objects is initialized to 0"""
        self.assertEqual(getattr(Base, "_Base_nb_objects"), 0)

    def test_5(self):
        """Test Base instantiation"""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, ("id": 1))
        self.assertEqual(b.id, 1)

    if __name__ = "__main__":
        unittest.main()
