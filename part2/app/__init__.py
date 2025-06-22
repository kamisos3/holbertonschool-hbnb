from flask import Flask, Blueprint
from flask_restx import Api

def create_app():
    app = Flask(__name__)

    blueprint = Blueprint('api', __name__)
    api = Api(
        blueprint,
        version='1.0',
        title='HBnB API',
        description='__init__: HBnB Accommodation Service API',
        doc='/doc',
        prefix='/api/v1'
    )

    app.register_blueprint(blueprint, url_prefix='/api/v1')

    from app.api.v1 import register_namespaces
    register_namespaces(api)

    return app
