#!/usr/bin/python3
"""Base class for my Review model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """The base class for my Review model"""

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
