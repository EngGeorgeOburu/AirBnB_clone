#!/usr/bin/python3
"""
Initfile for the models module
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
