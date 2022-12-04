#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the User class."""
=======
""" User Class """
>>>>>>> c87c406edb7130ed6b26dca0105301a7d197c9f5
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

=======
    """ User class that inherits BaseModel """
>>>>>>> c87c406edb7130ed6b26dca0105301a7d197c9f5
    email = ""
    password = ""
    first_name = ""
    last_name = ""
