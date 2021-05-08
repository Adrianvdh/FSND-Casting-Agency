import datetime
import json
from unittest import mock

from casting_agency.extensions import db
from casting_agency.models import Gender
from tests.factories import MovieFactory, GenreFactory, ActorFactory
from tests.mocks import token_response, casting_assistant_payload, casting_director_payload, executive_producer_payload
from tests.utils import BaseTestCase


class MoviesAPITest(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.genre = GenreFactory(name='Kids')
        self.movie_1 = MovieFactory(title='Movie 1', description='Some description', release_date=self.today,
                                    duration=120)
        db.session.commit()

    def test_access(self):
        """
        Test that access to this resource is protected.
        """
        res = self.client.get('/api/movies')
        assert res.status_code == 401

        res = self.client.get(f'/api/movies/{self.movie_1.id}')
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

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', casting_assistant_payload)
    def test_get_moviedetail_for_casting_assistant(self):
        """
        Test that a casting assistant user may list movies.
        """
        res = self.client.get(f'/api/movies/{self.movie_1.id}')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == self.movie_1.serialize()


class ActorsAPITest(BaseTestCase):

    def setUp(self):
        super().setUp()
        self.actor = ActorFactory(full_name='Brad Pitt', description='Cool guy',
                                  date_of_birth=datetime.date(1963, 12, 18), height=186, gender=Gender.Male,
                                  cover_image_url='file.jpg')
        db.session.commit()

    def test_access(self):
        """
        Test that access to this resource is protected.
        """
        res = self.client.get('/api/actors')
        assert res.status_code == 401

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', casting_assistant_payload)
    def test_get_actors_list_for_casting_assistant(self):
        """
        Test that a casting assistant user may list actors.
        """
        res = self.client.get('/api/actors')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == [self.actor.serialize()]

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', casting_director_payload)
    def test_get_movies_list_for_casting_director(self):
        """
        Test that a casting casting user may list actors.
        """
        res = self.client.get('/api/actors')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == [self.actor.serialize()]

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_get_movies_list_for_executive_producer(self):
        """
        Test that a executive producer user may list actors.
        """
        res = self.client.get('/api/actors')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == [self.actor.serialize()]
