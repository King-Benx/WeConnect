from flask import Blueprint
api = Blueprint('api', __name__)
from . import authentication, errors, business, reviews, user
