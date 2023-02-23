#!/usr/bin/python3
"""
Module that tests differents
behaviors of the BaseModel class
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class BaseModel(unittest.TestCase):
    """
    A class to tests BaseModel
    """

    def test_init(self):
        """ Tests init
        """
        model = BaseModel()
        model.id = '667a709e-c2e8-4dd4-aed0-4cb97e9bcb20'
        self.assertEqual(model.id, '667a709e-c2e8-4dd4-aed0-4cb97e9bcb20')

        model.created_at = "datetime.datetime(2023, 2, 23, 1, 48, 35, 129484)"
        self.assertEqual(model.created_at,
                         "datetime.datetime(2023, 2, 23, 1, 48, 35, 129484)")

        model.updated_at = "datetime.datetime(2023, 2, 23, 1, 48, 35, 129484)"
        self.assertEqual(model.updated_at,
                         "datetime.datetime(2023, 2, 23, 1, 48, 35, 129484)")

    def test_save(self):
        """ Test method save updates the public instance attribute """
        model = BaseModel()
        update = model.updated_at
        model.save()
        self.assertNotEqual(update, model.updated_at)

    def test_to_dict(self):
        """Test method to_dict"""
        model = BaseModel()
        newdict = model.to_dict()
        self.assertIsInstance(newdict, dict)
        self.assertTrue("__class__" in newdict)
        self.assertIn('created_at', self.model.to_dict())
