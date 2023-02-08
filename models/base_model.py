#!/usr/bin/python3
"""This class represents the base class for all my models"""

from datetime import datetime
import uuid

class BaseModel:
    """The base model class for my models"""

    def __init__(self, *args, **kwargs):
        """Method that initializes the object"""
        self.__set_attributes(kwargs)

    def __set_attributes(self, attr_dict):
        """Sets the attributes of a model instance based on **kwargs or default values"""
        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid.uuid4())
        for attr in ['created_at', 'updated_at']:
            if attr not in attr_dict:
                attr_dict[attr] = datetime.now()
            elif not isinstance(attr_dict[attr], datetime):
                attr_dict[attr] = datetime.strptime(
                    attr_dict[attr], "%Y-%m-%dT%H:%M:%S.%f")
        for attr, value in attr_dict.items():
            if attr == '__class__':
                continue
            setattr(self, attr, value)

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
