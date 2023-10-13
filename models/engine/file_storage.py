#!/usr/bin/env python3
"""Defines the FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstract dtorage engine.

    Attributes:
        __file_path (str): The name of file to save objects to
        __objects (dict): A dictionary of objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to JSON file __file_path."""
        objdict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserelize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for key, value  in obj_dict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return


