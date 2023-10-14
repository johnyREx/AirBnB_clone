#!/usr/bin/env python3
"""
Module defines State class that inherits BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class defines the State"""
    state_id = ""
    name = ""
