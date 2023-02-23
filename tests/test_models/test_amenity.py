#!/usr/bin/python3
""" test Amenity """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ unittest for Amenity file """

    def test_name(self):
        """ test attribute name """
        amenity = Amenity()
        self.assertEqual("", amenity.name)
