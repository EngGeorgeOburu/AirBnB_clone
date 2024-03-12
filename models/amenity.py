#!/usr/bin/python3
"""
Module for Amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class Amenity that inherits from BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes Amenity instance
        """
        super().__init__(*args, **kwargs)
        self.name = ""
