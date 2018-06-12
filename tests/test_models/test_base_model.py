#!/usr/bin/python3
"""test for BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """this will test the base model class"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base1 = BaseModel()
        cls.base1.name = "Kev"
        cls.base1.num = 20

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base1

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes_BaseModel(self):
        """chekcing if Basemodel have instance attribute"""
        self.assertTrue(hasattr(BaseModel, "__init__"))

    def test_init(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        base1_dict = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
