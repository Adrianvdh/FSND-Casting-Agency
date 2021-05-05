from flask import Blueprint, jsonify

from casting_agency.auth import requires_auth
from casting_agency.exceptions import ResourceNotFound
from casting_agency.models import Movie

blueprint = Blueprint('movies', __name__)


@blueprint.route('/api/movies', methods=('GET',))
@requires_auth(permission='get:movies')
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.serialize() for movie in movies])


@blueprint.route('/api/movies/<movie_id>', methods=('GET',))
@requires_auth(permission='get:movie-detail')
def get_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).first()
    if not movie:
        raise ResourceNotFound({
            'code': 'movie_not_found',
            'description': 'Resource not found!'
        }, 404)
    return jsonify(movie.serialize())
