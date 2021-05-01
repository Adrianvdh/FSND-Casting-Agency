from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from casting_agency.database import db
from casting_agency.models import Movie, Genre


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class GenreFactory(BaseFactory):

    class Meta:
        model = Genre


class MovieFactory(BaseFactory):

    class Meta:
        model = Movie
