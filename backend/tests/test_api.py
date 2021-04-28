import json
from tests.utils import BaseTestCase


class APITestCase(BaseTestCase):

    def test_get_hello_world(self):
        res = self.client.get('/')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == {
            'message': 'Hello world!'
        }
