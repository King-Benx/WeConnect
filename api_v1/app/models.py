import random
from . import users, known_user_ids, known_emails, businesses, known_business_ids, reviews, known_review_ids
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self, username, email, password):
        self.id = self.generate_user_id()
        self.username = username
        self.email = email
        self.password_hash = self.generate_password(password)
        self.create_user()

    def create_user(self):
        global users
        global known_emails
        new_user = dict()
        if self.email in known_emails:
            return 'Email exists'
        else:
            data = [self.username, self.password_hash, self.email]
            new_user[self.id] = data
            users.append(new_user)
            known_emails.append(self.email)

    def generate_user_id(self):
        global known_user_ids
        x = random.randint(1, 1000)
        if x not in known_user_ids:
            known_user_ids.append(x)
            return x
        else:
            self.generate_user_id()

    def generate_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user(user_id):
        for user in users:
            if user_id in user.keys():
                return user[user_id]


class Business:
    def __init__(self):
        pass


class Review:
    def __init__(self):
        pass
