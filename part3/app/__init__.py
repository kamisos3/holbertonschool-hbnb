from flask import Flask, Blueprint
from config import DevelopmentConfig
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.api.v1 import api_v1, api, register_namespaces

bcrypt = Bcrypt()

def create_app(config_class="config.DevelopmentConfig"):   # Defines config class
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['JWT_SECRET_KEY'] = 'hbnb-project-pt3'

    blueprint = Blueprint('api', __name__)
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='__init__: HBnB Accommodation Service API',
        )

    register_namespaces(api)
    app.register_blueprint(api_v1)

    return app
