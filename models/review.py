#!/usr/bin/env python3
"""
Module defines State class that inherits BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines the State"""
    place_id = ""
    user_id = ""
    text = ""
