from datetime import date, datetime

from flask import Blueprint, jsonify, request

from casting_agency.auth import requires_auth
from casting_agency.exceptions import ResourceNotFound, BadRequest, InternalServerError
from casting_agency.models import Actor

blueprint = Blueprint('actors', __name__)


@blueprint.route('/api/actors', methods=('GET',))
@requires_auth(permission='get:actors')
def get_actors():
    actors = Actor.query.all()
    return jsonify([actor.serialize() for actor in actors])


@blueprint.route('/api/actors/<actor_id>', methods=('GET',))
@requires_auth(permission='get:actor-detail')
def get_actor(actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).first()
    if not actor:
        raise ResourceNotFound({
            'code': 'actor_not_found',
            'description': 'Resource not found!'
        }, 404)
    return jsonify(actor.serialize())


def validate_body():
    body = request.get_json()
    if not body:
        raise BadRequest('You must include a body!')
    return body


def validate_actor_request(body):
    full_name = body.get('full_name', None)
    description = body.get('description', None)
    date_of_birth = body.get('date_of_birth', None)
    height = body.get('height', None)
    gender = body.get('gender', None)
    cover_image_url = body.get('cover_image_url', None)

    errors = []
    if not full_name:
        errors.append({'full_name': 'Full name field cannot be blank!'})
    if not description:
        errors.append({'description': 'Description field cannot be blank!'})
    if not date_of_birth:
        errors.append({'date_of_birth': 'Date of Birth field cannot be blank!'})
    if not height:
        errors.append({'release_date': 'Height field cannot be blank!'})
    if not gender:
        errors.append({'gender': 'Gender field cannot be blank!'})
    if not cover_image_url:
        errors.append({'cover_image_url': 'Cover image URL field cannot be blank!'})

    if date_of_birth:
        try:
            date_of_birth: date = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        except Exception:
            errors.append({'date_of_birth': 'The date_of_birth date should be in the format YYYY-MM-DD!'})

    if len(errors) > 0:
        raise BadRequest(errors)

    return cover_image_url, date_of_birth, description, full_name, gender, height


@blueprint.route('/api/actors', methods=('POST',))
@requires_auth(permission='post:actors')
def post_actor():
    body = validate_body()
    cover_image_url, date_of_birth, description, full_name, gender, height = validate_actor_request(body)

    try:
        actor = Actor(
            full_name=full_name,
            description=description,
            date_of_birth=date_of_birth,
            height=height,
            gender=gender,
            cover_image_url=cover_image_url
        )
        actor.insert()

        return jsonify({
            'success': True,
            'created': actor.id
        }), 201
    except Exception:
        raise InternalServerError('An internal server error occurred when saving the actor.')
