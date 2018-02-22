import unittest
from app.models import Review
from app import reviews


class ReviewTestCase(unittest.TestCase):
    def test_class_is_instance(self):
        # Tests that an object is an instance
        review1 = Reviewreview1 = Review(1, 1, 'review 1')
        self.assertIsInstance(review1, Review)

    def test_generate_review_id(self):
        # Tests that a unique id is created
        review1 = Review(1, 1, 'review 1')
        review2 = Review(1, 1, 'review 2')
        self.assertNotEqual(review1.id, review2.id)

    def test_create_business(self):
        # Tests to check whether a review has been created
        review = Review(1, 1, 'review 1')
        self.assertNotEqual(len(reviews), 0)
