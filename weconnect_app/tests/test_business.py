import unittest
from app.models import Business
from app import businesses


class BusinessTestCase(unittest.TestCase):
    def test_class_instance(self):
        # Tests that an object is an instance of a class
        business = Business(1, 'test business', 'inland', 'technology',
                            'business description')
        self.assertIsInstance(business, Business)

    def test_generate_business_id(self):
        # Tests that a unique id is created
        business1 = Business(1, 'test business', 'inland', 'technology',
                             'business description')
        business2 = Business(1, 'test business', 'overseas', 'technology',
                             'business description')
        self.assertNotEqual(business1.id, business2.id)

    def test_create_business(self):
        # Tests to check whether a business has been created
        business1 = Business(1, 'test business', 'inland', 'technology',
                             'business description')
        self.assertNotEqual(len(businesses), 0)
