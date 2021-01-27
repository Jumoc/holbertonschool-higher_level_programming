from models.rectangle import Rectangle
import models.rectangle
import unittest
from io import StringIO
from unittest.mock import patch
import pep8
import os


class TestBase(unittest.TestCase):
    """Test Cases for class Rectangle"""

    def test_pep8_conformance(self):
        """Check for pep8"""
        fchecker = pep8.Checker('models/rectangle.py', show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc(self):
        """Check if class and methods are documented
        haven't checked for module"""
        self.assertIsNotNone(models.rectangle.__doc__)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)

    def test_instances(self):
        """Check if instances id's are correctly assigned """
        self.rect1 = Rectangle(1, 2, id=10)
        self.rect2 = Rectangle(3, 4, id=20)
        self.rect3 = Rectangle(5, 6, id=30)

        self.assertEqual(self.rect1.id, 10)
        self.assertEqual(self.rect2.id, 20)
        self.assertEqual(self.rect3.id, 30)

    def test_width(self):
        """Checks width constraints"""
        self.r1 = Rectangle(1, 1)
        #Check for typeError
        with self.assertRaises(TypeError):
            self.r1.width = "10"
        with self.assertRaises(TypeError):
            self.r1.width = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.r1.width = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.r1.width = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.r1.width = 0
        with self.assertRaises(ValueError):
            self.r1.width = -10

    def test_height(self):
        """Checks height constraints"""
        self.r1 = Rectangle(1, 1)
        #Check for typeError
        with self.assertRaises(TypeError):
            self.r1.height = "10"
        with self.assertRaises(TypeError):
            self.r1.height = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.r1.height = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.r1.height = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.r1.height = 0
        with self.assertRaises(ValueError):
            self.r1.height = -10

    def test_x(self):
        """Checks x constraints"""
        self.r1 = Rectangle(1, 1)
        #Check for typeError
        with self.assertRaises(TypeError):
            self.r1.x = "10"
        with self.assertRaises(TypeError):
            self.r1.x = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.r1.x = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.r1.x = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.r1.x = -10

    def test_y(self):
        """Checks y constraints"""
        self.r1 = Rectangle(1, 1)
        #Check for typeError
        with self.assertRaises(TypeError):
            self.r1.x = "10"
        with self.assertRaises(TypeError):
            self.r1.x = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.r1.x = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.r1.x = 3.1415
        #Check for ValueError
        with self.assertRaises(ValueError):
            self.r1.x = -10

    def test_area(self):
        self.r1 = Rectangle(10, 5)
        self.assertEqual(self.r1.area(), 50)

    def test_display(self):
        r1 = Rectangle(2, 3, 2, 2)
        s1_rect = "\n\n  ##\n  ##\n  ##\n"

        r2 = Rectangle(3, 2, 1, 0)
        s2_rect = " ###\n ###\n"

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), s1_rect)

        with patch('sys.stdout', new = StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), s2_rect)

    def test_str(self):
        Rectangle.__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1, 2, 1)

        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (1) 1/2 - 5/5\n")

    def test_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9, 10)
        dictionary = r1.to_dictionary()
        test_dict = {
            "id": 10, "width": 10, "height": 2,
            "x": 1, "y": 9
        }

        self.assertEqual(dictionary, test_dict)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10, 1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        r1.update(89)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (89) 10/10 - 10/10\n")

        r1.update(89, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (89) 10/10 - 2/10\n")

        r1.update(89, 2, 3)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (89) 10/10 - 2/3\n")

        r1.update(89, 2, 3, 4)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (89) 4/10 - 2/3\n")

        r1.update(89, 2, 3, 4, 5)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

        r1.update(x=1, height=2, y=3, width=4)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (89) 1/3 - 4/2\n")
