#!/usr/bin/python3
""" test state """
import unittest
from models.base_model import BaseModel
from models.state import State


class Test_State(unittest.TestCase):
    """ unittest for state file """

    def test_name(self):
        state = State()
        self.assertEqual("", state.name)
