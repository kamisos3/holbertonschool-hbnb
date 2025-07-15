from flask import Flask, Blueprint
from config import DevelopmentConfig
from app.extensions import bcrypt, jwt


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['JWT_SECRET_KEY'] = 'hbnb-project-pt3'

    from app.api.v1 import api_v1


    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(api_v1)


    from flask import redirect
    @app.route('/')
    def index():
        return redirect('/api/v1/')

    return app
