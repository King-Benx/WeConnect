from . import main
from flask import render_template


@main.app_errorhandler('404')
def page_not_known(e):
    
    return render_template('404.html'), 404


@main.app_errorhandler('500')
def internal_server_error(e):
    return render_template('505.html'), 500
