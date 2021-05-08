from flask import Blueprint, jsonify

from casting_agency.auth import requires_auth
from casting_agency.models import Actor

blueprint = Blueprint('actors', __name__)


@blueprint.route('/api/actors', methods=('GET',))
@requires_auth(permission='get:actors')
def get_actors():
    actors = Actor.query.all()
    return jsonify([actor.serialize() for actor in actors])
