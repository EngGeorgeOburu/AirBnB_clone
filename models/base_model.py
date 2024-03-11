#!/usr/bin/python3
"""
This defines the BaseModel class.
"""

import models
import uuid
from datetime import datetime

class BaseModel:
    """ Base module for all other classes."""

    def __init__(self, *args, **kwargs):
        """
        Inirializing an instance of the base class .

        Args:
            *args: Variables argument list
            **kwargs:  Keyword arguements
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__classes__":
                    setattr(self, key, value)
                if key == 'updated_at' or key == 'created_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.id = self.updated_at = self.created_at = datetime.now()
    def __str__(self):
        """
        Prints a string representation of the base class.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Returns adictionary representaton of the instance 

        Returns:
            dict: A dictioanry containing all attributes of the instance
        """
        self.updated_at = datetime.now()
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
