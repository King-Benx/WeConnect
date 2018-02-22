import unittest
from werkzeug.security import check_password_hash
from app.models import User
from app import users


class UserTestCase(unittest.TestCase):
    def test_generate_password(self):
        # Tests that a password hash is unique and that its not the same as the previous value
        user = User('derrick', 'derrick@mail.com', 'password')
        user2 = User('susan', 'susan@mail.com', 'password')
        result = user.generate_password('password')
        result2 = user2.generate_password('password')
        self.assertNotEqual(result, result2)
        self.assertNotEqual(user.password_hash, 'password')

    def test_verify_password(self):
        # Tests that we can verify a password
        user = User('derrick', 'derrick@mail.com', 'password')
        result = user.verify_password('password')
        self.assertEqual(
            check_password_hash(user.password_hash, 'password'), result)
        self.assertNotEqual(
            check_password_hash(user.password_hash, 'pass'), result)

    def test_generate_user_id(self):
        # Tests that an id is totally random
        user = User('derrick', 'derrick@mail.com', 'password')
        user2 = User('susan', 'susan@mail.com', 'password')
        self.assertNotEqual(user.id, user2.id)

    def test_email(self):
        # Tests that an email has to be unique
        user = User('derrick', 'derrick@mail.com', 'password')
        user2 = User('susan', 'susan@mail.com', 'password')
        self.assertNotEqual(user2.email, user.email)

    def test_user_created(self):
        # Tests that a user has been created
        user = User('derrick', 'derrick@mail.com', 'password')
        self.assertNotEqual(len(users), 0)
