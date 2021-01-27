from models.square import Square
import models.square
import unittest
from io import StringIO
from unittest.mock import patch
import pep8
import os


class TestBase(unittest.TestCase):
    """Test Cases for class Rectangle"""

    def setUp(self):
        self.s1 = Square(2, 5, 7, 10)
        self.s2 = Square(5, 0, 1, 30)
        self.s3 = Square(5, 0, 1, 50)

    def test_pep8_conformance(self):
        """Check for pep8"""
        fchecker = pep8.Checker('models/square.py', show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc(self):
        """Check if class and methods are documented
        haven't checked for module"""
        self.assertIsNotNone(models.square.__doc__)
        self.assertIsNotNone(Square.__doc__)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_instances(self):
        """Check if instances id's are correctly assigned """
        self.assertEqual(self.s1.id, 10)
        self.assertEqual(self.s2.id, 30)
        self.assertEqual(self.s3.id, 50)

    def test_width(self):
        """Checks width constraints"""
        #Check for typeError
        with self.assertRaises(TypeError):
            self.s1.width = "10"
        with self.assertRaises(TypeError):
            self.s2.width = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.s3.width = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.s1.width = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.s1.width = 0
        with self.assertRaises(ValueError):
            self.s1.width = -10

    def test_height(self):
        """Checks height constraints"""
        #Check for typeError
        with self.assertRaises(TypeError):
            self.s1.height = "10"
        with self.assertRaises(TypeError):
            self.s2.height = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.s3.height = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.s1.height = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.s1.height = 0
        with self.assertRaises(ValueError):
            self.s1.height = -10

    def test_size(self):
        """Checks for size"""
        #Check for typeError
        with self.assertRaises(TypeError):
            self.s1.size = "10"
        with self.assertRaises(TypeError):
            self.s2.size = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.s3.size = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.s1.size = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.s1.size = 0
        with self.assertRaises(ValueError):
            self.s1.size = -10

    def test_sizewh(self):
        self.assertEqual(self.s1.size, self.s1.width)
        self.assertEqual(self.s1.size, self.s1.height)
        self.assertEqual(self.s2.size, self.s2.width)
        self.assertEqual(self.s2.size, self.s2.height)

    def test_x(self):
        """Checks x constraints"""
        #Check for typeError
        with self.assertRaises(TypeError):
            self.s1.x = "10"
        with self.assertRaises(TypeError):
            self.s2.x = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.s1.x = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.s1.x = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.s1.x = -10

    def test_y(self):
        """Checks y constraints"""
        #Check for typeError
        with self.assertRaises(TypeError):
            self.s1.x = "10"
        with self.assertRaises(TypeError):
            self.s1.x = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.s1.x = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.s1.x = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.s1.x = -10

    def test_area(self):
        self.assertEqual(self.s1.area(), 4)

    def test_dictionary(self):
        square1 = Square(10, 2, 1, 10)
        dictionary = square1.to_dictionary()
        test_dict = {
            "id": 10, "size": 10,
            "x": 2, "y": 1
        }

        self.assertEqual(dictionary, test_dict)

    def test_update(self):
        s1 = Square(5, id=1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), "[Square] (1) 0/0 - 5\n")

        s1.update(10)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), "[Square] (10) 0/0 - 5\n")

        s1.update(1, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), "[Square] (1) 0/0 - 2\n")

        s1.update(1, 2, 3)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), "[Square] (1) 3/0 - 2\n")

        s1.update(1, 2, 3, 4)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), "[Square] (1) 3/4 - 2\n")

        s1.update(x=12)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), "[Square] (1) 12/4 - 2\n")

        s1.update(size=7, y=1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), "[Square] (1) 12/1 - 7\n")
