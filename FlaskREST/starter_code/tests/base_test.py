# this class should be the parent class to each non-unit test.
# it allows for instance of th database dynamically and make sure that it is a new, blank database each time

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    def setUp(self):
        # Make sure database exists
        app.config['SQL_DATABASE'] = 'sqlite:///'
        with app.app_context():
           db.init_app(app)
           db.create_all()
        # Get a test client
        self.app = app.test_client()
        self.app = app.app_context
        pass

    def tearDown(self):
        # database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()

