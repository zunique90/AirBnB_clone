#!/usr/bin/python3
# This module creates a unique FileStorage instance for use in my models

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
