from flask import Flask, Blueprint
from config import DevelopmentConfig
from flask_restx import Api
from app.extensions import bcrypt, jwt


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['JWT_SECRET_KEY'] = 'hbnb-project-pt3'

    from app.api.v1 import api_v1, register_namespaces

    bcrypt.init_app(app)
    jwt.init_app(app)

    blueprint = Blueprint('api', __name__)
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Accommodation Service API'
    )
    register_namespaces(api)
    app.register_blueprint(api_v1)

    return app
