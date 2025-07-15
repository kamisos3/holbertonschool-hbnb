from werkzeug.security import check_password_hash 
from flask_restx import Namespace, Resource, fields
from app.services import HBnBFacade
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

ns = Namespace('users', description='User operations')

facade = HBnBFacade()

user_model = ns.model('User', {
    'first_name': fields.String(
        required=True,
        description='First name of the user',
        max_lenght=50
    ),
    'last_name': fields.String(
        required=True,
        description='Last name of the user',
        max_lenght=50
    ),
    'email': fields.String(
        required=True,
        description='Email address of the user',
        pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    ),
    'is_admin': fields.Boolean(
        description='Admin privileges status',
        default=False
    )
})

user_update_model = ns.model('UserUpdate', {
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
    'is_admin': fields.Boolean(description='Admin status')
})

user_response = ns.model('User_Response', {
    'id': fields.String(description='Unique user ID'),
    'first_name': fields.String(description='First name'),
    'last_name': fields.String(description='Last name'),
    'email': fields.String(description='Email address'),
    'is_admin': fields.Boolean(description='Admin status')
})

login_model = ns.model('Login', {
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='User password')
})

@ns.route('/')
class UserList(Resource):
    @ns.expect(user_model, validate=True)
    @ns.response(201, 'User created successfully', user_response)
    @ns.response(400, 'Validate error')
    def post(self):
        user_data = ns.payload

        if facade.get_user_by_email(user_data['email']):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
            return {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email,
                'password': new_user.password,
                'is_admin': new_user.is_admin
                }, 201   # User created successfully

            facade.user_repo.save(new_user)

        except ValueError as e:
            return {'error': str(e)}, 400

    @ns.response(200, 'User list retrieved', [user_response])
    @ns.marshal_list_with(user_response)
    def get(self):
        users = facade.user_repo.get_all()
        return users, 200

@ns.route('/<string:user_id>')
class UserResource(Resource):
    @ns.response(200, 'User details retrieved', user_response)
    @ns.response(404, 'User not found')
    def get(self, user_id):
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'is_admin': user.is_admin
        }, 200

    @jwt_required()
    @ns.expect(user_model, validate=False)
    @ns.response(200, 'User updated successfully', user_response)
    @ns.response(400, 'Validation error')
    @ns.response(404, 'User not found')
    def put(self, user_id):
        current_user = get_jwt_idenity()
        if current_user['id'] != user_id:
            return {'error': 'Unauthorized action'}, 403

        update_data = ns.payload

        if 'email' in update_data or 'password' in update_data:
            return {'error': 'You cannot modify email or password'}, 400

        user = facade.user_repo.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        try:
            for key, value in update_data.items():
                setattr(user, key, value)
            facade.user_repo.update(user_id, update_data)

            return {
                'id': updated_user.id,
                'first_name': updated_user.first_name,
                'last_name': update_user.last_name,
                'email': update_user.email,
                'is_admin': updated_user.is_admin
            }, 200
        except ValueError as e:
            return {'error': str(e)}, 400

@ns.route('/login')
class UserLogin(Resource):
    @ns.expect(login_model)
    @ns.response(200, 'Login successful')
    @ns.response(401, 'Invalid credentials')
    def post(self):
        data = ns.payload
        user = facade.get_user_by_email(data['email'])
        if not user or not check_password_hash(user.password, data['password']):
            return {'error': 'Invalid credentials'}, 401

        token = create_access_token(identity={'id': user.id, 'is_admin': user.is_admin})
        return {'access_token': token}, 200
