import datetime

from casting_agency.extensions import db
from casting_agency.models import Movie, Actor, Genre, Gender
from tests.factories import GenreFactory, MovieFactory, ActorFactory
from tests.utils import BaseTestCase


class MovieModelTests(BaseTestCase):

    def test_create_and_read(self):
        genre = GenreFactory(name='Kids')
        movie = MovieFactory(title='Bee Movie', description='A movie about bees', genre=genre,
                             release_date=datetime.date(2007, 5, 8), duration=90, cover_image_url='file.jpg')
        db.session.commit()

        read_movie = Movie.query.filter(Movie.id == movie.id).first()
        assert read_movie.serialize() == {
            'title': 'Bee Movie',
            'description': 'A movie about bees',
            'genre': 'Kids',
            'release_date': '2007-05-08',
            'duration': 90,
            'cover_image_url': 'file.jpg'
        }

    def test_delete(self):
        movie = MovieFactory(title='Movie 1')
        assert Movie.query.count() == 1

        movie.delete()
        assert Movie.query.count() == 0


class ActorModelTests(BaseTestCase):

    def test_create_and_read(self):
        actor = ActorFactory(full_name='Brad Pitt', description='Cool guy', date_of_birth=datetime.date(1963, 12, 18),
                             height=186, gender=Gender.MALE, cover_image_url='file.jpg')
        db.session.commit()

        read_actor = Actor.query.filter(Actor.id == actor.id).one_or_none()
        assert read_actor.serialize() == {
            'full_name': 'Brad Pitt',
            'description': 'Cool guy',
            'date_of_birth': '1963-12-18',
            'height': 186,
            'gender': 'Male',
            'cover_image_url': 'file.jpg'
        }

    def test_delete(self):
        actor = ActorFactory(full_name='Brad Pitt')
        db.session.commit()
        assert Actor.query.count() == 1

        actor.delete()
        assert Actor.query.count() == 0
