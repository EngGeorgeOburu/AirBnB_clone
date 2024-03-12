#!/usr/bin/python3
"""
Moule for the state
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is a class that represents a user.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.
        """
        super().__init__(**kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
