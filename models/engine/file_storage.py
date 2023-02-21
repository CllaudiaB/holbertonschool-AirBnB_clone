#!/usr/bin/python3
"""
    Module that defines a new class: FileStorage
"""

import json
import os.path

class FileStorage:
    """
        Module that serializes instances to a a JSON
        file and desearializez JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ 
            Returns the dictionary of __objects
            <ob class name>.id
        """

        return FileStorage.__objects
    
    def new(self, obj):
        """
            sets in __objects the obj with key 
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            Sets in __objects to the JSON file
            (path: __file_path)
        """

        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
            Deserializes the JSON file to __objects
        """

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    obj = cls(**obj_data)
                    self.__objects[key] = obj