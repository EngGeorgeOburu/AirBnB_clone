#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Class review that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of review class
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
