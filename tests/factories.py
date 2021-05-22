from factory.alchemy import SQLAlchemyModelFactory

from casting_agency.database import db
from casting_agency.models import Movie, Genre, Actor


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class ActorFactory(BaseFactory):

    class Meta:
        model = Actor


class GenreFactory(BaseFactory):

    class Meta:
        model = Genre


class MovieFactory(BaseFactory):

    class Meta:
        model = Movie
