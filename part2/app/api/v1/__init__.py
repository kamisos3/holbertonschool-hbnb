"""__init__ initializes the v1 API package"""
from .reviews import ns as reviews_ns

def register_namespaces(api):
    from .users import ns as users_ns
    from .places import ns as places_ns
    from .reviews import ns as reviews_ns
    from .amenities import ns as amenities_ns

    api.add_namespace(users.ns, path='/users')
    api.add_namespace(places.ns)
    api.add_namespace(reviews.ns, path='/api/v1/reviews')
    api.add_namespace(amenities.ns)
