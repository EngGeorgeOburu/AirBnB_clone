#!/usr/bin/python3
"""
Module for state city
"""


from models.base_model import BaseModel

class State(BaseModel):
    """
    State class that inherits from the BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the instance of a new state.
        """
        super().__init__(*args, **kwargs)
        self.state = ""
