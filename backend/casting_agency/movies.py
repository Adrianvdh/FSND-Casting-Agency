from flask import Blueprint, jsonify

from casting_agency.auth import requires_auth
from casting_agency.models import Movie

blueprint = Blueprint('movies', __name__)


@blueprint.route('/api/movies', methods=('GET',))
@requires_auth(permission='get:movies')
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.serialize() for movie in movies])
