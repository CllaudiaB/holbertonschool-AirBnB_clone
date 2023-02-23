#!/usr/bin/python3
""" test city """
import unittest
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """ unittest for city file """
    def test_instance(self):
        "Test instance"
        city = City()
        self.assertIsInstance(city, City)

    def test_city_name(self):
        "Test city name"
        city = City()
        self.assertEqual("", city.name)

    def test_id(self):
        "Test id"
        city = City()
        self.assertEqual(str, type(city.id))

    def test_state_id(self):
        "Test state id"
        city = City()
        self.assertEqual("", city.state_id)
