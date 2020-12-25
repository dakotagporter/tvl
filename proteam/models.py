"""Instantiation of web app users"""

from flask_login import UserMixin
from . import DB


class User(UserMixin, DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(100), unique=True)
    password = DB.Column(DB.String(100))
    name = DB.Column(DB.String(1000))
