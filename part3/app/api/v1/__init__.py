"""__init__ initializes the v1 API package"""
from .auth import ns as auth_ns
from .users import ns as users_ns
from .places import ns as places_ns
from .reviews import ns as reviews_ns
from .amenities import ns as amenities_ns
from flask_restx import Api
from flask import Blueprint

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(api_v1, version='1.0', title="HBnB API")

def register_namespaces(api):
    api.add_namespace(auth.ns, path='/api/v1/auth')
    api.add_namespace(users.ns, path='/api/v1/users')
    api.add_namespace(places.ns, path='/api/v1/places')
    api.add_namespace(reviews.ns, path='/api/v1/reviews')
    api.add_namespace(amenities.ns, path='/api/v1/amenities')
