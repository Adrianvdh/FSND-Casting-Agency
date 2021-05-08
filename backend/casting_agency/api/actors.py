from flask import Blueprint, jsonify

from casting_agency.auth import requires_auth
from casting_agency.exceptions import ResourceNotFound
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
