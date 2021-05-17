from datetime import datetime, date

from flask import Blueprint, jsonify, request

from casting_agency.auth import requires_auth
from casting_agency.exceptions import ResourceNotFound, BadRequest, InternalServerError
from casting_agency.models import Movie, Genre

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


def validate_movie_request(body):
    title = body.get('title', None)
    description = body.get('description', None)
    genre = body.get('genre', None)
    release_date = body.get('release_date', None)
    duration = body.get('duration', None)
    cover_image_url = body.get('cover_image_url', None)

    errors = []
    if not title:
        errors.append({'title': 'Title field cannot be blank!'})
    if not description:
        errors.append({'description': 'Description field cannot be blank!'})
    if not genre:
        errors.append({'genre': 'Genre field cannot be blank!'})
    if not release_date:
        errors.append({'release_date': 'Release date field cannot be blank!'})
    if not duration:
        errors.append({'duration': 'Duration field cannot be blank!'})
    if not cover_image_url:
        errors.append({'cover_image_url': 'Cover image URL field cannot be blank!'})

    if release_date:
        try:
            release_date: date = datetime.strptime(release_date, '%Y-%m-%d').date()
        except Exception:
            errors.append({'release_date': 'The release date should be in the format YYYY-MM-DD!'})

    if len(errors) > 0:
        raise BadRequest(errors)
    return cover_image_url, description, duration, genre, release_date, title


def validate_body():
    body = request.get_json()
    if not body:
        raise BadRequest('You must include a body!')
    return body


@blueprint.route('/api/movies', methods=('POST',))
@requires_auth(permission='post:movies')
def post_movie():
    body = validate_body()
    cover_image_url, description, duration, genre, release_date, title = validate_movie_request(body)

    try:
        genre_q = Genre.query.filter(Genre.name == genre).one_or_none()
        if not genre_q:
            genre = Genre(name=genre)
            genre.insert()

        movie = Movie(
            title=title,
            description=description,
            genre=genre_q,
            release_date=release_date,
            duration=duration,
            cover_image_url=cover_image_url
        )
        movie.insert()
        return jsonify({
            'success': True,
            'created': movie.id
        }), 201
    except Exception:
        raise InternalServerError('An internal server error occurred when saving the movie.')


@blueprint.route('/api/movies/<movie_id>', methods=('DELETE',))
@requires_auth(permission='delete:movies')
def delete_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).first()
    if not movie:
        raise ResourceNotFound('Movie not found!')
    Movie.query.filter(Movie.id == movie_id).delete()
    return jsonify({
        'success': True,
        'delete': movie_id
    }), 200


@blueprint.route('/api/movies/<movie_id>', methods=('PATCH',))
@requires_auth(permission='patch:movies')
def update_movie(movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).first()
    if not movie:
        raise ResourceNotFound('Movie not found!')

    body = validate_body()
    cover_image_url, description, duration, genre, release_date, title = validate_movie_request(body)

    try:
        genre_obj = Genre.query.filter(Genre.name == genre).one_or_none()
        if not genre_obj:
            genre_obj = Genre(name=genre)
            genre_obj.insert()

        movie.title = title
        movie.description = description
        movie.genre = genre_obj
        movie.release_date = release_date
        movie.duration = duration
        movie.cover_image_url = cover_image_url
        movie.update()

        return jsonify({
            'success': True,
            'updated': movie.id
        }), 200
    except Exception as e:
        raise InternalServerError('An internal server error occurred when updating the movie.')
