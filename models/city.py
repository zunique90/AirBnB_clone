#!/usr/bin/python3
"""Base class for my City model"""

from models.base_model import BaseModel


class City(BaseModel):
    """The base class for my City model"""

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
