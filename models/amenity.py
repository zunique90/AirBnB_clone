#!/usr/bin/python3
"""Base class for my Amenity model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """The base class for my Amenity model"""

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
