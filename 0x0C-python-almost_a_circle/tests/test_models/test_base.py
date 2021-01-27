from models.base import Base
from models.rectangle import Rectangle
import models.base
import unittest
import pep8
import os


class TestBase(unittest.TestCase):
    """Test Cases for class Base"""

    def test_pep8_conformance(self):
        """Check for pep8"""
        fchecker = pep8.Checker('models/base.py', show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc(self):
        """Check if class and methods are documented
        haven't checked for module"""
        self.assertIsNotNone(models.base.__doc__)
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_instances(self):
        """Check if instances id's are correctly assigned """
        self.b1 = Base()
        self.assertEqual(self.b1.id, 1)
        self.b2 = Base()
        self.assertEqual(self.b2.id, 2)
        self.b3 = Base()
        self.assertEqual(self.b3.id, 3)
        self.b4 = Base(12)
        self.assertEqual(self.b4.id, 12)
        self.b5 = Base()
        self.assertEqual(self.b5.id, 4)

    def test_tojson(self):
        """Check if to_json_string converts a list of dicts
        and Null check"""
        dict_1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dict_1])
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(json_dictionary,
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(json_dictionary, "[]")

    def test_jsonstring(self):
        """Check if from_json_string converts from string to an object"""
        string_1 = '[{"a": 1, "b": 2}]'
        list_1 = [{"a": 1, "b": 2}]
        self.assertEqual(Base.from_json_string(string_1), list_1)
        self.assertEqual(Base.from_json_string(None), [])

    #def test_create(self):
        #r1 = Rectangle(1, 2)
        #r2 = Base.create(**r1.to_dictionary())
        #self.assertEqual(r1, r2)
