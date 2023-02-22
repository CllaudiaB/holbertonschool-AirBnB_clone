#!/usr/bin/python3
""" create class city """
from models.base_model import BaseModel


class City(BaseModel):
    """ class that inherit from BaseModel """
    state_id = ""
    name = ""
