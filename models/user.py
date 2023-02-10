#!/usr/bin/python3
"""Base class for my User model"""

from models.base_model import BaseModel


class User(BaseModel):
    """The base class for my User model"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
