#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the Review class."""
=======
""" Class Review """
>>>>>>> c87c406edb7130ed6b26dca0105301a7d197c9f5
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

=======
    """ Review class that inherits BaseModel """
>>>>>>> c87c406edb7130ed6b26dca0105301a7d197c9f5
    place_id = ""
    user_id = ""
    text = ""
