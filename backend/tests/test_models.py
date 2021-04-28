import datetime

from casting_agency.models import Movie, Actor, Genre, Gender
from tests.utils import BaseTestCase


class MovieModelests(BaseTestCase):

    def test_create_and_read(self):
        kids = Genre(name='Kids')
        kids.insert()
        movie = Movie(title='Bee Movie', description='A movie about bees', genre_id=kids.id,
                      release_date=datetime.date(2007, 5, 8), duration=90, cover_image_url='file.jpg')
        movie.insert()

        read_movie = Movie.query.filter(Movie.id == movie.id).one_or_none()
        assert read_movie.serialize() == {
            'title': 'Bee Movie',
            'description': 'A movie about bees',
            'genre': 'Kids',
            'release_date': '2007-05-08',
            'duration': 90,
            'cover_image_url': 'file.jpg'
        }

    def test_delete(self):
        movie = Movie(title='Bee Movie')
        movie.insert()
        assert Movie.query.count() == 1

        movie.delete()
        assert Movie.query.count() == 0


class ActorModelTests(BaseTestCase):

    def test_create_and_read(self):
        actor = Actor(full_name='Brad Pitt', description='Cool guy', date_of_birth=datetime.date(1963, 12, 18),
                      height=186, gender=Gender.MALE, cover_image_url='file.jpg')
        actor.insert()

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
        actor = Actor(full_name='Brad Pitt')
        actor.insert()
        assert Actor.query.count() == 1

        actor.delete()
        assert Actor.query.count() == 0
