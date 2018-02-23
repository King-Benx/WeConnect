from flask import render_template, url_for
from . import main


@main.route('/')
def index():
    register_user = str(url_for('api.register_new_user', _external=True))
    logout_user = str(url_for('api.logout_user', _external=True))
    reset_password = str(url_for('api.reset_password', _external=True))
    login = str(url_for('api.login', _external=True))
    context = {
        'register_user': register_user,
        'logout_user': logout_user,
        'reset_password': reset_password,
        'login': login
    }
    return render_template('index.html', context=context)
