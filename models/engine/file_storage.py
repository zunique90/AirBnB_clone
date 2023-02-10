#!/usr/bin/python3
"""This module contains the model for the FileStorage model"""

import os
import json


class FileStorage:
    """The model that describes the engine for file storage"""

    __file_path = 'file.json'
    __objects = {}

    def generate_key(self, object_id=None, object_classname=None, objekt=None):
        """
        Generates a string to be used as key for object_id
        Arguments:
            object_id: id of the object (can be omitted if objekt is provided)
            object_classname: Class name of the object (can be omitted if objekt is provided)
            objekt: the objekt (can be omitted if object_id and object_classname are provided)
        Returns:
            A string. This string is empty if certain conditions are not meant.
            Check the Arguments section
        """

        key = ''
        if objekt:
            key = "{}.{}".format(objekt.__class__.__name__, objekt.id)
        elif object_id and object_classname:
            key = "{}.{}".format(object_classname, object_id)

        return key

    def update_object(self, objekt):
        """
        Updates the object in __self.objects
        Arguments:
            (object) objekt: the object to be updated
        """
        key = self.generate_key(objekt=objekt)
        if key in self.__objects:
            self.__objects[key] = objekt.to_dict()

    def all(self):
        """
        Gets all object in storage
        Returns:
            A dictionary containing all object in storage
        """
        return self.__objects

    def get_all(self, _name):
        """
        Returns all objects in the storage that belongs to the `name` model
        Arguments:
            _name: the name of the model
        Returns:
            A dictionary containing all object under the model `name`
        """
        return {k: v for k, v in self.__objects.items() if _name in k}

    def new(self, objekt):
        """
        Adds a new item to the __objects dict
        Arguments:
            (object) objekt: the object to be added to storage
        """
        key = self.generate_key(objekt=objekt)
        self.__objects[key] = str(objekt)

    def save(self):
        """Serializes __objects to the JSON file at self.__file_path"""
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

    def in_storage(self, object_id=None, object_classname=None, key=None):
        """
        Checks if object with key of "key" exists in storage
        Or generates key from object_id and object_classname
        Arguments:
            (string) object_id: The object's id
            (string) object_classname: The object's class name(string)
            (string) key: the key of the object
        Returns:
            True if in storage else False
        """
        if not key and (object_id and object_classname):
            key = self.generate_key(object_id, object_classname)
        obj_in_storage = False
        for _key in self.__objects:
            if key == _key:
                obj_in_storage = True
                break
        return obj_in_storage

    def get_object(self, object_id=None, object_classname=None, key=None):
        """
        Gets object from storage with key of object_key.
        Or generates key from object_id and object_classname
        Arguments:
            object_id: The object's id
            object_classname: The object's class name
            (string) key: the key of the object
        Returns:
            None if object doesn't exists else the object's data
        """
        if not key and (object_id and object_classname):
            key = self.generate_key(object_id, object_classname)

        if self.in_storage(key=key):
            return self.__objects[key]
        return None

    def destroy_object(self, key):
        """
        Reomves an object from the storage
        Arguments:
            (key) key: the key of the object to be destroyed
        """
        status = False # Not deleted yet
        if self.in_storage(key=key):
            self.__objects.pop(key)
            self.save()
            status = True # Successfully deleted

        return status
