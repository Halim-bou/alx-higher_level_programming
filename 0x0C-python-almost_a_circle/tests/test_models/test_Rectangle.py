#!/usr/bi/python3
"""
all unittest for class Rectangle
"""
import io
import unittest
from rectangle import Rectangle
from base import Base


class Test_Rectangle_instances(unittest.TeseCase):
    """all test methods for instances of the class"""
    def test_Rectangle_with_Base(self):
        self.assertIsInstance(Rectangle(10, 5).Base)

    def test_Rectangle_0_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_Rectangle_1_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_Rectangle_2_args(self):
        Rec1 = Rectangle(10, 5)
        Rec2 = Rectangle(5, 10)
        self.assertEqual(Rec1, Rec2 - 1)

    def test_Rectangle_3_args(self):
        Rec1 = Rectangle(5, 5, 10)
        Rec2 = Rectangle(10, 10, 5)
        self.assertEqual(Rec1, Rec2 - 1)

    def test_Rectangle_3_args(self):
        Rec1 = Rectangle(10, 11, 12, 13)
        Rec2 = Rectangle(13, 12, 11, 10)
        self.assertEqual(Rec1, Rec2 - 1)

    def test_Rectangle_5_args(self):
        self.assertEqual(2, Rectangle(10, 20, 0, 0, 2).id)

    def test_Rectangle_to_much_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 30, 40, 50, 60)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 0, 0, 1).__widt)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 0, 0, 1).__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 0, 0, 1).__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        rec = Rectangle(10, 5, 5, 5, 1)
        self.assertEqual(10, rec.width)

    def test_width_setter(self):
        rec = Rectangle(10, 5, 5, 5, 1)
        rec.width = 5
        self.assertEqual(5, rec.width)

    def test_height_getter(self):
        rec = Rectangle(10, 5, 5, 5, 1)
        self.assertEqual(5, rec.height)

    def test_height_setter(self):
        rec = Rectangle(10, 5, 5, 5, 1)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_x_getter(self):
        rec = Rectangle(10, 5, 5, 5, 1)
        self.assertEqual(5, rec.x)

    def test_x_setter(self):
        rec = Rectangle(10, 5, 5, 5, 1)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_y_getter(self):
        rec = Rectangle(10, 5, 5, 5, 1)
        self.assertEqual(5, rec.y)

    def test_y_setter(self):
        rec = Rectangle(10, 5, 5, 5, 1)
        rec.y = 10
        self.assertEqual(10, rec.y)


