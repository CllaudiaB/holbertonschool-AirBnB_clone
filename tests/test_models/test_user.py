#!/usr/bin/python3
""" test user """
import unittest
from models.base_model import BaseModel
from models.user import User
import datetime
from io import StringIO


class TestUser(unittest.TestCase):
    """ unittest for user file """

    def test_email(self):
        user = User()
        user.email = "julien.barbier@holbertonschool.com"
        self.assertEqual(user.email, "julien.barbier@holbertonschool.com")

    def test_password(self):
        user = User()
        user.password = "Cloud-IA"
        self.assertEqual(user.password, "Cloud-IA")

    def test_first_name(self):
        user = User()
        user.first_name = "Julien"
        self.assertEqual(user.first_name, "Julien")

    def test_last_name(self):
        user = User()
        user.last_name = "Barbier"
        self.assertEqual(user.last_name, "Barbier")

    user = User()

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_user_inheritance(self):
        """test if User is a subclass of BaseModel"""
        self.assertIsInstance(self.user, User)

    def test_class_exist(self):
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")
