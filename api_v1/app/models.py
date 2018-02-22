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
        # creates a new user
        global users
        global known_emails
        generated_id = self.id
        if self.email not in known_emails:
            new_user = dict()
            data = [self.username, self.password_hash, self.email]
            new_user[generated_id] = data
            users.append(new_user)
            known_emails.append(self.email)

    def generate_user_id(self):
        # generate a unique user id for a new user
        global known_user_ids
        x = random.randint(1, 1000)
        if x not in known_user_ids:
            known_user_ids.append(x)
            return x
        else:
            self.generate_user_id()

    @staticmethod
    def generate_password(password):
        # generate a hashed password
        return generate_password_hash(password)

    def verify_password(self, password):
        # verify that passwords at login will match
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user(user_id):
        # get a user by id
        for user in users:
            if user_id in user.keys():
                return user[user_id]

    @staticmethod
    def login(email, password):
        # authenticate user
        for known_email in known_emails:
            if known_email['email'] == email:
                user_id = known_email['id']
                if check_password_hash(User.get_user(user_id)[1], password):
                    return True
                else:
                    return False


class Business:
    def __init__(self, user_id, name, location, category, description):
        self.id = self.generate_business_id()
        self.user_id = user_id
        self.name = name
        self.location = location
        self.category = category
        self.description = description
        self.create_business()

    def generate_business_id(self):
        # generate a business id
        global known_business_ids
        x = random.randint(1, 1000)
        if x not in known_business_ids:
            known_business_ids.append(x)
            return x
        else:
            self.generate_business_id()

    def create_business(self):
        # create a business
        global businesses
        new_business = dict()
        data = [
            self.user_id, self.name, self.location, self.category,
            self.description
        ]
        new_business[self.id] = data
        businesses.append(new_business)

    @staticmethod
    def get_business_by_id(business_id):
        pass

    @staticmethod
    def get_business_by_user(user_id):
        pass

    @staticmethod
    def delete_business(id):
        pass

    def covert_to_json(self):
        # serializable dictionary that defines business layout
        information = {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'location': self.location,
            'description': self.description
        }
        return information


class Review:
    def __init__(self, user_id, business_id, review):
        self.id = self.generate_review_id()
        self.user_id = user_id
        self.business_id = business_id
        self.review = review
        self.create_review()

    def create_review(self):
        # create review
        global reviews
        new_review = dict()
        data = [self.user_id, self.business_id, self.review]
        new_review[self.id] = data
        reviews.append(new_review)

    def generate_review_id(self):
        # generate a unique id for a review
        global known_review_ids
        x = random.randint(1, 1000)
        if x not in known_review_ids:
            known_review_ids.append(x)
            return x
        else:
            self.generate_review_id()

    @staticmethod
    def get_review_by_id(id):
        pass

    @staticmethod
    def get_review_by_business(business_id):
        pass

    def convert_to_json(self):
        information = {
            'id': self.id,
            'user_id': self.user_id,
            'business_id': self.business_id,
            'review': self.review
        }
        return information
