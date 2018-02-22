from flask import request, jsonify, url_for
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
