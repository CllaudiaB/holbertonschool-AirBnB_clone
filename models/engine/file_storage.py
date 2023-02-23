#!/usr/bin/python3
"""
    Module that defines a new class: FileStorage
"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(new_dict, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as json_file2:
                new_dict = json.load(json_file2)
                cls = "__class__"
                for key, value in new_dict.items():
                    class_name = key.split('.')
                    FileStorage.__objects[key] = eval(value[cls] + '(**value)')
        except FileNotFoundError:
            pass
