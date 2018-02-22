from flask import g
from flask_httpauth import HttpBasicAuth
from ..models import User
from .errors import forbidden, unauthorized
from . import api

auth = HttpBasicAuth()


@api.before_request
@auth.login_required
def before_request():
    if not g.current_user.confirmed:
        return forbidden('You do not have access')


@auth.verify_user
def verify_user(email, password):
    g.current_user = User.get_user_by_email(email)
    return User.login(email, password)


@auth.error_handler
def auth_error():
    return unauthorized('invalid credentials')
