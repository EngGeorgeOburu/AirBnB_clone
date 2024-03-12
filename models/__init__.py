#!/usr/bin/python3
"""Initializing the package."""

from models.base_model import BaseModel
from models import BaseModel
from .user import User
from .state import State
from .city import City
from .amenity import Amenity
from .review import Review
from .place import Place
from models.engine.file_storage import FileStorage

classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review,
        'Place': Place,
    }

storage = FileStorage()
storage.reload()
