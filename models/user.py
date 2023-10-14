#!/usr/bin/env python3
"""
Module defines User class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class inherits from BaseModel and defines a user.

    Attributes:
        email (str): the email of the user.
        password (str): the password of the user.
        first_name (str): the first name of the user.
        last_name (str): the last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
