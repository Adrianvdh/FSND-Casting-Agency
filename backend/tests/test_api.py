import unittest
import json

from casting_agency import create_app, db


class APITestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app('tests.config')
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        # self.db.session.commit()

    def test_get_hello_world(self):
        res = self.client().get('/')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == {
            'message': 'Hello world!'
        }