from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity

ns = Namespace('Review', description='Review related operations')

review_model = ns.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating (1-5)'),
    'user_id': fields.String(required=True, description='User ID'),
    'place_id': fields.String(required=True, description='Place ID')
})

simple_review_model = ns.model('SimpleReview', {
    'id': fields.String,
    'text': fields.String,
    'rating': fields.Integer
})

@ns.route('/')
class ReviewList(Resource):
    @jwt_required()
    @ns.expect(review_model)
    @ns.response(201, 'Review created')
    @ns.response(400, 'Invalid input')
    def post(self):
        current_user = get_jwt_identity()
        data = ns.payload

        data['user_id'] = current_user['id']

        place = facade.get_place(data['place_id'])
        if not place:
            return {"error": "Place not found"}, 404

        if place.owner_id == current_user['id']:
            return {"error": "You cannot review your own place"}, 400

        existing = facade.get_user_review_for_place(current_user['id'], data['place_id'])
        if existing:
            return {"error": "You havr already reviewed this place"}, 400

        try:
            review = facade.create_review(data)
            return vars(review), 201
        except ValueError as e:
            return {"error": str(e)}, 400

@ns.route('/<review_id>')
class ReviewResource(Resource):
    @ns.response(200, 'Success')
    @ns.response(404, 'Not found')
    def get(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return vars(review), 200

    @jwt_required()
    @ns.expect(review_model)
    @ns.response(200, 'Updated')
    @ns.response(404, 'Not found')
    @ns.response(400, 'Invalid data')
    def put(self, review_id):
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        if review.user_id != current_user['id']:
            return {"error": "Unauthorized action"}, 403
        data = ns.payload
        updated = facade.update_review(review_id, data)
        if not updated:
            return {"error": "Review not found"}, 404
        return {"message": "Review updated successfully"}, 200

    @jwt_required()
    @ns.response(204, 'Review deleted')
    def delete(self, review_id):
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        current_user = get_jwt_identity()
        if review.user_id != current_user['id']:
            return {"error": "Unauthorized action"}, 403
        facade.delete_review(review_id)
        return {}, 204

@ns.route('/places/<place_id>/reviews')
class PlaceReviews(Resource):
    @ns.response(200, 'Success')
    @ns.response(404, 'Place not found')
    def get(self, place_id):
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        reviews = facade.get_reviews_by_place(place_id)
        return [vars(r) for r in reviews], 200
