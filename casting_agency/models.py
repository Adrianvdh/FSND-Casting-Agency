import datetime
from enum import Enum
from casting_agency.database import BaseModel, db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#


def date_format(date: datetime.date) -> str:
    return date.strftime('%-d %B %Y')


class Genre(BaseModel):
    __tablename__ = 'Genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    movie = db.relationship('Movie', back_populates='genre')

    def __str__(self):
        return self.name


class Cast(BaseModel):
    __tablename__ = 'Cast'

    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'), primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'), primary_key=True)

    movie = db.relationship('Movie', back_populates='cast')  # back_populates Movie.cast
    actor = db.relationship('Actor', back_populates='movies')  # back_populates Actor.movies


class Movie(BaseModel):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(500))
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'))
    release_date = db.Column(db.Date())
    duration = db.Column(db.Integer())
    cover_image_url = db.Column(db.String(500))

    cast = db.relationship('Cast', back_populates='movie')
    genre = db.relationship('Genre', back_populates='movie')

    def serialize(self):
        return {
            **self.serialize_movie(),
            **self.serialize_cast(),
        }

    def serialize_cast(self):
        return {
            'cast': [cast.actor.serialize_actor() for cast in self.cast]
        }

    def serialize_movie(self):
        def _minutes_format(minutes: int) -> str:
            h, m = divmod(minutes, 60)
            return f'{h:d}h {m:02d}m'

        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'genre': str(self.genre),
            'release_date': date_format(self.release_date),
            'duration': _minutes_format(self.duration),
            'cover_image_url': self.cover_image_url,
        }


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'


class Actor(BaseModel):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    description = db.Column(db.String(500))
    date_of_birth = db.Column(db.Date())
    height = db.Column(db.Integer())
    gender = db.Column(db.Enum(Gender))
    cover_image_url = db.Column(db.String(500))

    movies = db.relationship('Cast', back_populates='actor')

    def serialize(self):
        return {
            **self.serialize_actor(),
            **self.serialize_movies(),
        }

    def serialize_movies(self):
        return {
            'movies': [cast.movie.serialize_movie() for cast in self.movies]
        }

    def serialize_actor(self):
        def _height_format(height: int) -> str:
            h, m = divmod(height, 100)
            return f'{h:d}m {m:02d}cm'

        return {
            'id': self.id,
            'full_name': self.full_name,
            'description': self.description,
            'date_of_birth': date_format(self.date_of_birth),
            'height': _height_format(self.height),
            'gender': self.gender.value,
            'cover_image_url': self.cover_image_url
        }
