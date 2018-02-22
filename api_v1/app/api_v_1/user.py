from flask import request, jsonify, url_for, session
from . import api
from .authentication import auth
from ..models import User


@api.route('/api/v1/auth/register', methods=['POST'])
def register_new_user():
    # register new user into the system
    data = request.get_json()
    if len(data.keys()) == 3:
        username = data['username']
        email = data['email']
        password = data['password']
        user = User(username, email, password)
        if user:
            return jsonify({
                'message':
                'Successfully created user ' + str(username) +
                ' you can login using ' +
                str(url_for('api.login', _external=True))
            })
        else:
            return jsonify({'message': 'Failure creating user'})
    else:
        return jsonify({
            'message': 'Couldn\'t create user, some fields missing'
        })


@api.route('/api/vi/auth/logout', methods=['POST'])
def logout_user():
    # This logs out user from the application
    sign_out = User.logout()
    if sign_out == True:
        print(session.get('id'))
        print(session.get('status'))
        return jsonify({'message': 'You have been successfully logout'})
    else:
        return jsonify({
            'message':
            'Something went wrong, please try again ' +
            str(url_for('api.logout_user',_external=True))
        })

@api.route('/api/vi/auth/reset-password ', methods=['POST'])
def reset_password():
    # This logs out user from the application
    pass