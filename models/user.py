#!/usr/bin/env python3
"""
Module defines User class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class inherits from BaseModel and defines a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
