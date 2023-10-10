#!/usr/bin/env python3
"""
BaseModel class defines all common attributes/methods for other classess
"""

from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """This class defines all common methods/attributes"""
    def __init__(self, *args, **kwargs):
        """Initialize class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                elif key == "__class__":
                    continue
                if "id" not in kwargs.keys():
                    self.id = str(uuid.uuid4())
                if "created_at" not in kwargs.keys():
                    self.created_at = datetime.now()
                if "updated_at" not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ Overrides __str__ """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary with all keys/values of __dict__"""
        d = self.__dict__.copy()
        d["__class__"] = type(self).__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
