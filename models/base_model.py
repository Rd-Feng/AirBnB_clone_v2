#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
from datetime import datetime


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """

    def __init__(self):
        """Instantiation of base model class
        Args:

        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            str(type(self).__name__), self.id, str(self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = self.__dict__
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
