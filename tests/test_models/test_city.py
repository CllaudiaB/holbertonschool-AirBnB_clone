#!/usr/bin/python3
""" test city """
import unittest
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """ unittest for city file """
	def test_state_id(self):
        """ test attribute state_id """
        city = City()
        city.state_id = ""
        self.assertEqual(city.state_id, "")

    def test_name(self):
        """ test attribute name """
        city = City()
        city.name = ""
        self.assertEqual(city.name, "")
