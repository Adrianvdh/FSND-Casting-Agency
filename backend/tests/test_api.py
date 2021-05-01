import json
from unittest import mock
from tests.factories import MovieFactory, GenreFactory
from tests.mocks import token_response, casting_assistant_payload, casting_director_payload, executive_producer_payload
from tests.utils import BaseTestCase


class MoviesAPITest(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.genre = GenreFactory(name='Kids')
        self.movie_1 = MovieFactory(title='Movie 1', description='Some description', release_date=self.today,
                                    duration=120)

    def test_access(self):
        """
        Test that acess to this resource is protected.
        """
        res = self.client.get('/api/movies')
        assert res.status_code == 401

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', casting_assistant_payload)
    def test_get_movies_list_for_casting_assistant(self):
        """
        Test that a casting assistant user may list movies.
        """
        res = self.client.get('/api/movies')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == [self.movie_1.serialize()]

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', casting_director_payload)
    def test_get_movies_list_for_casting_director(self):
        """
        Test that a casting casting user may list movies.
        """
        res = self.client.get('/api/movies')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == [self.movie_1.serialize()]

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_get_movies_list_for_executive_producer(self):
        """
        Test that a executive producer user may list movies.
        """
        res = self.client.get('/api/movies')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == [self.movie_1.serialize()]


