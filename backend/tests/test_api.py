import datetime
import json
from unittest import mock

from sqlalchemy import desc

from casting_agency.extensions import db
from casting_agency.models import Gender, Movie, Genre
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
    def test_get_movie_detail_for_casting_assistant(self):
        """
        Test that a casting assistant user retrieve a movie detail.
        """
        res = self.client.get(f'/api/movies/{self.movie_1.id}')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == self.movie_1.serialize()

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_post_movie(self):
        body = {
            'title': 'Bee Movie',
            'description': 'A movie about beets',
            'genre': 'Kids',
            'release_date': '2007-12-12',
            'duration': 90,
            'cover_image_url': 'file.jpg'
        }

        res = self.client.post(f'/api/movies', json=body)

        assert res.status_code == 201

        movie = Movie.query.order_by(desc(Movie.id)).first()
        data = json.loads(res.data)
        assert data['success']
        assert data['created'] == movie.id
        assert data == self.movie_1.serialize()

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_post_movie_new_genre(self):
        def genre_exists(name) -> bool:
            return db.session.query(Genre.query.filter(Genre.name == name).exists()).scalar()

        assert not genre_exists('Kids Adventure')
        body = {
            'title': 'Bee Movie',
            'description': 'A movie about beets',
            'genre': 'Kids Adventure',
            'release_date': '2007-12-12',
            'duration': 90,
            'cover_image_url': 'file.jpg'
        }

        res = self.client.post(f'/api/movies', json=body)

        assert res.status_code == 201
        assert genre_exists('Kids Adventure')

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_post_movie_with_invalid_release_date(self):
        body = {
            'title': 'Bee Movie',
            'description': 'A movie about beets',
            'genre': 'Kids',
            'release_date': '2007/12/12',
            'duration': 90,
            'cover_image_url': 'file.jpg'
        }

        res = self.client.post(f'/api/movies', json=body)

        assert res.status_code == 400

        data = json.loads(res.data)
        assert data == {
            'success': False,
            'error': 'Bad Request',
            'message': [
                {'release_date': 'The release date should be in the format YYYY-MM-DD!'}
            ]
        }

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_post_movie_no_body(self):

        res = self.client.post(f'/api/movies')

        assert res.status_code == 400

        data = json.loads(res.data)
        assert data == {
            'success': False,
            'error': 'Bad Request',
            'message': 'You must include a body!'
        }

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_post_movie_required_fields(self):
        body = {
            'title': '',
            'description': '',
            'genre': '',
            'release_date': '',
            'duration': '',
            'cover_image_url': ''
        }

        res = self.client.post(f'/api/movies', json=body)

        assert res.status_code == 400

        data = json.loads(res.data)
        assert data == {
            'success': False,
            'error': 'Bad Request',
            'message': [
                {'title': 'Title field cannot be blank!'},
                {'description': 'Description field cannot be blank!'},
                {'genre': 'Genre field cannot be blank!'},
                {'release_date': 'Release date field cannot be blank!'},
                {'duration': 'Duration field cannot be blank!'},
                {'cover_image_url': 'Cover image URL field cannot be blank!'},
            ]
        }

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_delete_movie(self):
        def movie_exists(m_id: int) -> bool:
            return db.session.query(Movie.query.filter(Movie.id == m_id).exists()).scalar()

        movie_id = self.movie_1.id
        assert movie_exists(movie_id)

        res = self.client.delete(f'/api/movies/{movie_id}')

        assert res.status_code == 200
        assert not movie_exists(movie_id)

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', executive_producer_payload)
    def test_delete_movie_not_found(self):
        res = self.client.delete(f'/api/movies/{123}')

        assert res.status_code == 404
        data = json.loads(res.data)
        assert data == {
            'success': False,
            'error': 'Resource Not Found',
            'message': 'Movie not found!'
        }


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

    @mock.patch('casting_agency.auth.get_token_auth_header', token_response)
    @mock.patch('casting_agency.auth.verify_decode_jwt', casting_assistant_payload)
    def test_get_actor_detail_for_casting_assistant(self):
        """
        Test that a casting assistant user retrieve an actor detail.
        """
        res = self.client.get(f'/api/actors/{self.actor.id}')

        assert res.status_code == 200
        data = json.loads(res.data)
        assert data == self.actor.serialize()
