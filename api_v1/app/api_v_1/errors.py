from flask import jsonify


def created_resource(message):
    # helper functions when resources have been created and there is need for a custom message
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 201
    return response


def forbidden(message):
    # helper function when there is something lacking in the users authentication information
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def method_not_allowed(message):
    # in the event a user send a request that has an unacceptable method
    response = jsonify({'error': 'method not allowed', 'message': message})
    response.status_code = 405
    return response


def bad_request(message):
    # to handle invalid requests
    response = jsonify({'error': 'method not allowed', 'message': message})
    response.status_code = 405
    return response
