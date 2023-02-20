#!/usr/bin/python3
import uuid
from datetime import datetime
""" 
class BaseModel is a parent class 
"""


class BaseModel:
    """ 
    define all common attributes/methods for other classes 
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        string representation of BaseModel
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ 
        updates the public instance attribute
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = __class__.__name__
        new_dict["created_at"] = datetime.isoformat(self.created_at)
        new_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return new_dict