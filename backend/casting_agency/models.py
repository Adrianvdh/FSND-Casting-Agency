from enum import Enum
from casting_agency.database import BaseModel, db


# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#

class Casting(BaseModel):
    __tablename__ = 'Casting'

    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'), primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'), primary_key=True)

    movie = db.relationship('Movie', back_populates='casting')
    actor = db.relationship('Actor', back_populates='casting')


class Genre(BaseModel):
    __tablename__ = 'Genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    movie = db.relationship('Movie', back_populates='genre')

    def __str__(self):
        return self.name


class Movie(BaseModel):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    description = db.Column(db.String(500))
    genre_id = db.Column(db.Integer, db.ForeignKey('Genre.id'))
    release_date = db.Column(db.Date())
    duration = db.Column(db.Integer())
    cover_image_url = db.Column(db.String(500))

    casting = db.relationship('Casting', back_populates='movie')
    genre = db.relationship('Genre', back_populates='movie')

    def serialize(self):
        return {
            'title': self.title,
            'description': self.description,
            'genre': str(self.genre),
            'release_date': str(self.release_date),
            'duration': self.duration,
            'cover_image_url': self.cover_image_url
        }


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


class Actor(BaseModel):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120))
    description = db.Column(db.String(500))
    date_of_birth = db.Column(db.Date())
    height = db.Column(db.Integer())
    gender = db.Column(db.Enum(Gender))
    cover_image_url = db.Column(db.String(500))

    casting = db.relationship('Casting', back_populates='actor')

    def serialize(self):
        return {
            'full_name': self.full_name,
            'description': self.description,
            'date_of_birth': str(self.date_of_birth),
            'height': self.height,
            'gender': self.gender.value,
            'cover_image_url': self.cover_image_url
        }
