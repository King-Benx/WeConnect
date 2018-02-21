import os
from app import create_app
from app.models import User, Business, Review
from flask_script import Manager
from flask_script import Shell

app = create_app(os.getenv('APPLICATION_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, User=User, Business=Business, Review=Review)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
