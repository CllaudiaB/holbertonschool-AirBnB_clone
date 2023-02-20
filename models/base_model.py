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
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

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
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "__class__": __class__.__name__
        }
