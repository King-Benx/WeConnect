from flask import Flask
from config import config

# variables to store data in memory
users = []
known_user_ids = []
reviews = []
known_review_ids = []
businesses = []
known_business_ids = []
known_emails = []


def create_app(config_name):
    # instantiate the application and packages required
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # create blueprint of main
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # create blueprint of the api
    from .api_v_1 import api as api_blueprint
    app.register_blueprint(api_blueprint)
    return app
