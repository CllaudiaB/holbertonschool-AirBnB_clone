#!/usr/bin/python3
""" test review """
import unittest
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """ unittest for review file """

    def test_place_id(self):
        """ test attribute place_id """
        review = Review()
        self.assertEqual("", review.place_id)

    def test_user_id(self):
        """ test attribute user_id """
        review = Review()
        self.assertEqual("", review.user_id)

    def test_text(self):
        """ test attribute text """
        review = Review()
        review.text = ""
        self.assertEqual(review.text, "")
