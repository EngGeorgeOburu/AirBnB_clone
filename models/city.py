#!/usr/bin/python3
"""
Module for city BaseModel
"""


from models.base_model import BaseModel

class City(BaseModel):
    """
    City class that inherits from the BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes instance of a city
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
