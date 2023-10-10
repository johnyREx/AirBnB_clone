#!/usr/bin/env python3
"""
Module defines State class that inherits BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines the State"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_integer = 0
    price_by_night = 0
    latitude  = 0.0
    longitude = 0.0
    amenity_id = []
