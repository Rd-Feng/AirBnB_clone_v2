#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''testing file storage'''

    @classmethod
    def setUpClass(cls):
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    @classmethod
    def teardown(cls):
        del cls.rev1

    def teardown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        melissa = User()
        melissa.id = 999999
        melissa.name = "Melissa"
        m_storage.new(melissa)
        key = melissa.__class__.__name__ + "." + str(melissa.id)
        #print(instances_dic[key])
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
