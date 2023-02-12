#!/usr/bin/python3
"""This class represents the base class for all my models"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """The base model class for my models"""

    def __init__(self, *args, **kwargs):
        """Method that initializes the object"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # If it's a new object, add it to the storage engine
            storage.new(self)

    def __set_attributes(self, attr_dict):
        """
        Sets the attributes of a model instance
        based on **kwargs or default values
        """
        attr_dict_new = {}
        for attr, value in attr_dict.items():
            if attr in ['created_at', 'updated_at']:
                if not isinstance(value, datetime):
                    attr_dict_new[attr] = datetime.strptime(
                        attr_dict[attr], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                attr_dict_new[attr] = value
        for attr, value in attr_dict_new.items():
            if attr == '__class__':
                continue
            setattr(self, attr, value)

    def __str__(self):
        """The string representation of the object"""
        return '[{0}] ({1}) {2}'.format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def __is_serializable(self, obj):
        """Checks if an object is serializable"""
        try:
            obj_to_string = json.dumps(obj)
            return obj_to_string is not None and isinstance(obj_to_string, str)
        except Exception:
            return False

    def save(self):
        """Saves the model instance"""
        self.updated_at = datetime.now()
        # Update the value in storage before saving the storage to file
        storage.update_object(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the model instance"""
        obj_to_dict = {**self.__dict__, '__class__': self.__class__.__name__}
        obj_to_dict['created_at'] = obj_to_dict['created_at'].isoformat()
        obj_to_dict['updated_at'] = obj_to_dict['updated_at'].isoformat()
        return obj_to_dict
