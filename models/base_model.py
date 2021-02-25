#!/usr/bin/python3
"""This module contains one class, BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents the base model class for the HBnB console"""
    def __init__(self, *args, **kwargs):
        """__init__ method called by every new instance"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        cls_name = self.__class__.__name__
        string = "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
        return string

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of the BaseModel Instance
        :return: dictionary containing key/value pairs of an object
        """
        mydict = self.__dict__.copy()
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        mydict["__class__"] = self.__class__.__name__
        return mydict
