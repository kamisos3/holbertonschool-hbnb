from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import create_access_token
from app.services import HBnBFacade
facade = HBnBFacade()

ns = Namespace('auth', description='Authentication operations')

login_model = ns.model('Login',{
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

@ns.route('/login')
class Login(Resource):
    @ns.expect(login_model)
    def post(self):
        credentials = ns.payload
        user = facade.get_user_by_email(credentials['email'])

        print('Stored hash:', user.password if user else None,
              'Attempt:', credentials['password'])
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401

        access_token = create_access_token(identity={'id': str(user.id), 'is_admin': user.is_admin})
        return {'access_token': access_token}, 200
