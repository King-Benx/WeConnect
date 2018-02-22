from flask import request, jsonify
from . import api
from .authentication import auth
from ..models import Review


@api.route('/api/v1/businesses/<businessId>/reviews', methods=['POST'])
@auth.login_required
def post_review():
    pass
