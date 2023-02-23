#!/usr/bin/python3
""" Test place """
import unittest
from models.base_model import BaseModel
from models.place import Place
from models.user import User
from models.city import City


class TestPlace(unittest.TestCase):
    """
    Test place file
    """
    def test_instance(self):
        """test the creation of a Place instance"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertTrue(type(place.city_id), str)
        self.assertTrue(type(place.user_id), str)
        self.assertTrue(type(place.name), str)
        self.assertTrue(type(place.description), str)
        self.assertTrue(type(place.number_rooms), int)
        self.assertTrue(type(place.number_bathrooms), int)
        self.assertTrue(type(place.max_guest), int)
        self.assertTrue(type(place.price_by_night), int)
        self.assertTrue(type(place.latitude), float)
        self.assertTrue(type(place.longitude), float)
        self.assertTrue(type(place.amenity_ids), list)
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
        self.assertEqual(len(place.amenity_ids), 0)
        city = City()
        place.city_id = city.id
        self.assertEqual(place.city_id, city.id)
        user = User()
        place.user_id = city.id
        self.assertEqual(place.user_id, city.id)

    def test_city_id(self):
        place = Place()
        place.city_id = "42"
        self.assertEqual(place.city_id, "42")

    def test_user_id(self):
        place = Place()
        place.user_id = "0626839210"
        self.assertEqual(place.user_id, "0626839210")

    def test_name(self):
        place = Place()
        place.name = "San Francisco"
        self.assertEqual(place.name, "San Francisco")

    def test_description(self):
        place = Place()
        place.description = "La maison de Julien Barbier"
        self.assertEqual(place.description, "La maison de Julien Barbier")

    def test_number_rooms(self):
        place = Place()
        place.number_rooms = 6
        self.assertEqual(place.number_rooms, 6)

    def test_bathrooms(self):
        place = Place()
        place.number_bathrooms = 3
        self.assertEqual(place.number_bathrooms, 3)

    def test_max_guest(self):
        place = Place()
        place.max_guest = 18
        self.assertEqual(place.max_guest, 18)

    def test_price_by_night(self):
        place = Place()
        place.price_by_night = 300
        self.assertEqual(place.price_by_night, 300)

    def test_latitude(self):
        place = Place()
        place.latitude = 37.77750
        self.assertEqual(place.latitude, 37.77750)

    def test_longitude(self):
        place = Place()
        place.longitude = -122.41639
        self.assertEqual(place.longitude, -122.41639)

    def test_amenity_ids(self):
        place = Place()
        place.amenity_ids = ["Computer", "Wifi", "Coffee Machine"]
        self.assertEqual(place.amenity_ids, [
            "Computer", "Wifi", "Coffee Machine"])
