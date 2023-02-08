#!/usr/bin/python3
"""This class represents the base class for all my models"""

from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """The string representation of the object"""
        return '[{0}] ({1}) {2}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Saves the model instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the model instance"""
        obj_to_dict = {**self.__dict__, '__class__': self.__class__.__name__}
        obj_to_dict['created_at'] = obj_to_dict['created_at'].isoformat()
        obj_to_dict['updated_at'] = obj_to_dict['updated_at'].isoformat()
        return obj_to_dict
