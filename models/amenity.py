#!/usr/bin/python3
"""Defines Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): Name of the amenity.
    """

    name = ""
