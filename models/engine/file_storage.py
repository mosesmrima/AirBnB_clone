#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""
This module contains the file storage class
which serializes and deserializes instances to JSON file
"""


class FileStorage:
    """
     Represents a storage engine to serialize and deserialize
     objects to a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns all entries of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new instance to __objects"""
        clsname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clsname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    obj = BaseModel(**o)
                    FileStorage.new(self, obj)
        except FileNotFoundError:
            return
