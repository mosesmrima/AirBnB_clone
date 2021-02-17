#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""This module contains one class, BaseModel"""


class BaseModel:
    """Represents the BaseModel of the HBnB project"""
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    tform = "%Y-%m-%dT%H:%M:%S.%f"
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
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

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clsname = self.__class__.__name__
        string = "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
        return string
