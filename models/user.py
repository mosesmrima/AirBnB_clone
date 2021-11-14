#!/usr/bin/python3
""" this module contains one class """

from models.base_model import BaseModel


class User(BaseModel):
    """User clas defination"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
