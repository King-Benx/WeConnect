from . import main
from flask import request, redirect, url_for
from flask import jsonify


@main.app_errorhandler('404')
def page_not_known(e):
    # handle errors in a json format for unknown urls
    if request.accept_mimtypes.accept_json and not request.accept_mimtypes.accept_html:
        response = jsonify({'error ': 'Page not Known'})
        response.status_code = 404
        return response


@main.app_errorhandler('500')
def internal_server_error(e):
    # incase an internal server error occurs due to some bug in the code
    if request.accept_mimtypes.accept_json and not request.accept_mimtypes.accept_html:
        response = jsonify({'error ': 'Internal Server Error'})
        response.status_code = 500
        return response
