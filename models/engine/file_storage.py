#!/usr/bin/python3

""" ths module contains the filestorage class """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """FileStorage class defination"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return a dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        objects = FileStorage.__objects
        dictionary = {k: objects[k].to_dict() for k in objects.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path)
        """
        try:
            with open(FileStorage.__file_path) as f:
                dictionary = json.load(f)
                for o in dictionary.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
