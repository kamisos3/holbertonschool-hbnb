#!/usr/bin/python3
from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1')

# Add API endpoints later and the items listed in pt1

    return app
