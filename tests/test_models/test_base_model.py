#!/usr/bin/python3
""" unit tests for BaseModel class """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """Unit tests suit for BaseModel """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_to_dict(self):
        """
        Tests that to_dict:
            - returns a dictionary
            - that contains all keys/values of __dict__
            - contains __class__ and that this __class__ is the class name
        """
        base = BaseModel()

        "Returns a dictionary"
        returned_dict = base.to_dict()
        self.assertIsInstance(returned_dict, dict)

        "Dictionary contains __class__, which is the class name"
        self.assertTrue("__class__" in returned_dict)
        self.assertEqual(returned_dict["__class__"], type(base).__name__)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)


if __name__ == '__main__':
    unittest.main()
