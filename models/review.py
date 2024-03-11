#!/usr/bin/python3
"""
Modelue for the review
"""


from models.base_model import BaseModel

class Review(BaseModel):
    """
    Class review that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes an instance of review class
        Args:
            *args: positional argument list
            **kwargs: keyword argument list
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
