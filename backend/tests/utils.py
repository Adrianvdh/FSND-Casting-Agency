from flask_testing import TestCase

from casting_agency import create_app
from casting_agency.extensions import db
from tests.config import TestConfig


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app(config_object=TestConfig)

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
