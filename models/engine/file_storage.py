#!/usr/bin/python3
"""Define FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Abstracted storage engine for managing objects.

    Attributes:

        __file_path (str): The path to the JSON file for saving objects.
        __objects (dict): A dictionary of instantiated objects.
    
    """

    def __init__(self):
        """Open FileStorage."""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Return back the dictionary of obj."""
        return self.__objects

    def save(self):
        """Save obj to the JSON."""
        obj_dict = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """reload the JSON file to obj."""
        try:
            with open(self.__file_path) as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    obj_instance = eval(cls_name)(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

    def new(self, obj):
        """Add a new object to obj."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
