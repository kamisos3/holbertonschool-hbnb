from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='__init__: Amenity management operations')

amenity_model = api.model('Amenity', {
    'name': fields.String(
        required=True,
        description='__init__: Name of amenity',
        max_lenght=50
    )
})

amenity_response = api.model('AmenityResponse', {
    'id': fields.String(description='__init__: Unique amenity ID'),
    'name': fields.String(description='__init__: Amenity name')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model, validate=True)
    @api.response(201, '__init__: Amenity created successfully', amenity_response)
    @api.response(400, '__init__: Validation error')
    def post(self):
        amenity_data = api.payload

        try:
            new_amenity = facade.create_amenity(amenity_data)
            return {
                    'id': new_amenity.id,
                    'name': new_amenity.name
                }, 201
        except ValueError as e:
            return {'error': f'__init__: {str(e)}'}, 400

    @api.response(200, '__init__: Amenity list retrieved', [amenity_response])
    def get(self):
        amenities = facade.get_all_amenities()
        return [{
            'id': amenity.id,
            'name': amenity.name
        } for amenity in amenities], 200

@api.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @api.response(200, '__init__: Amenity details retrieved', amenity_response)
    @api.response(404, '__init__: Amenity not found')
    def get(self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': '__init__: Amenity not found'}, 404
        return {
            'id': amenity.id,
            'name': amenity.name
        }, 200

    @api.expect(amenity_model, validate=False)
    @api.response(200, '__init__: Amenity updated successfully', amenity_response)
    @api.response(400, '__init__: Validation error')
    @api.response(404, '__init__: Amenity not found')
    def put (self, amenity_id):
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': '__init__: Amenity not found'}, 404

        update_data = api.payload

        try:
            updated_amenity = facade.update_amenity(amenity_id, update_data)
            if isinstance(updated_amenity, str):
                    return {'error': f'__init__: {updated_amenity}'}, 400
             return {
                'id': update_amenity.id,
                'name': update_amenity.name
            }, 200
        except Exception as e:
            return {'error': f'__init__: {str(e)}'}, 400
