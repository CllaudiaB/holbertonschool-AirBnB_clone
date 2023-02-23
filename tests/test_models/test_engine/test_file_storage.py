#!/usr/bin/python3
"""
Module that tests differents
behaviors of the FileStorage class
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime

class FileStorage(unittest.TestCase):
    """
    A class to tests FileStorage
    """
    def test_file_path(self):
        """Test path method"""
        file_storage = FileStorage()
        self.assertEqual(str, type(file_storage.FileStorage__file_path))

    def test_objects(self):
        """Test objects method"""
        file_storage = FileStorage()
        self.assertEqual(dict, type(file_storage._FileStorage__objects))

    def test_all(self):
        """Test all method"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Test the new method"""
        model = BaseModel()
        models.storage.new(model)
        self.assertIn("BaseModel." + model.id, models.storage.all().keys())
        self.assertIn(model, models.storage.all().values()

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        models.storage.new(model)
        models.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + model.id, save_text)

    def test_reload(self):
        """Test the reload method"""
        model = BaseModel()
        models.storage.new(model)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + model.id, obj)
