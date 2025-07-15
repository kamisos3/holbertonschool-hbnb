#!/usr/bin/python3
"""Initialize Flask extensions"""
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


bcrypt = Bcrypt()
jwt = JWTManager()
