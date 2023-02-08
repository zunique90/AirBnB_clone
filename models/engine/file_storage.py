#!/usr/bin/python3
"""This module contains the model for the FileStorage model"""

import os
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def update_object(self, key, value):
        """Updates the object with key of "key" in __self.objects"""
        if key in self.__objects:
            self.__objects[key] = value

    def all(self):
        """Returns all objects in the storage"""
        return self.__objects

    def new(self, obj):
        """Adds a new item to the __objects dict"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = str(obj)
        # 0078865858 fanegan deborah union bank

    def save(self):
        """Serializes __objects to the JSON file at self.__file_path"""
        # print(self.__objects)
        with open(self.__file_path, 'w', encoding='utf-8') as outFile:
            json.dump(self.__objects, outFile)
        # Just to add a newline to the end of the file
        with open(self.__file_path, 'a', encoding='utf-8') as outFile:
            outFile.write('\n')

    def reload(self):
        """Deserializes the JSON file at self.__file_path into self.__objects if
        the file exists. Raises no error, if the file doesn't exist"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path) as outFile:
                self.__objects = json.load(outFile)
