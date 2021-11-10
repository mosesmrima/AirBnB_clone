#!/usr/bin/env python3

""" This module contains the base class defination """

import uuid
from datetime import datetime
import json
import models


class BaseModel:
    """this is the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """init method"""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """update the updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """return a dictionary containing __dict__ of an instance"""
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if v:
                if k == "updated_at" or k == "created_at":
                    v = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
                my_dict[k] = v
        return my_dict
