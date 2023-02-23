#!/usr/bin/python3
"""
Class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Write a class User that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
