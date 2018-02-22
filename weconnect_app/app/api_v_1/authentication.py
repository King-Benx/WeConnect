from flask import g, jsonify, request, url_for, session
from flask_httpauth import HTTPBasicAuth
from ..models import User
from .errors import forbidden, unauthorized
from . import api
auth = HTTPBasicAuth()

# @api.before_request
# @auth.login_required
# def before_request():
#     if not g.current_user.confirmed:
#         return forbidden('You do not have access')


@auth.verify_password
def verify_password(email, password):
    g.current_user = User.get_user_by_email(email)
    return User.login(email, password)


@api.route('/api/v1/auth/login', methods=['POST'])
def login():
    # This logs user into system
    data = request.get_json()
    email = data['email']
    password = data['password']
    status = User.login(email, password)
    if status == True:
        return jsonify({'message': 'successfully logged in'})
    else:
        return jsonify({
            'message':
            'Failure logging in! if you are not registered use register using '
            + str(url_for('api.register_new_user', _external=True))
        })


@auth.error_handler
def auth_error():
    return unauthorized('invalid credentials')
