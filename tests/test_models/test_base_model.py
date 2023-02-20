#!/usr/bin/python3
"""
    Module that tests differents
    behaviors of the BaseModel class
"""
from models.base_model import BaseModel
import unittest
import uuid


class BaseModel(unittest.TestCase):
    """
        A class to tsts BaseModel
    """

    def test_init(self):
        """
            Tests atributes
        """

        model_1 = BaseModel()
        model_1.id = '667a709e-c2e8-4dd4-aed0-4cb97e9bcb20'
        self.assertEqual(model_1.id, '667a709e-c2e8-4dd4-aed0-4cb97e9bcb20')