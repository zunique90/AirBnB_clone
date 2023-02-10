#!/usr/bin/python3
"""Base class for my state model"""

from models.base_model import BaseModel


class State(BaseModel):
    """The base class for my State model"""

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
