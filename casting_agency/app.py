from flask import Flask, jsonify

from .api import movies, actors
from .exceptions import InternalServerError, BadRequest, ResourceNotFound
from .extensions import db, migrate, cors
from .auth import requires_auth, AuthError
from .config import DefaultConfig


def create_app(config_object=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_views(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)


def register_views(app):
    # Set up CORS. Allow '*' for origins
    origins = '*'
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    cors.init_app(movies.blueprint, origins=origins, resources={r"/*": {"origins": "*"}})
    cors.init_app(actors.blueprint, origins=origins, resources={r"/*": {"origins": "*"}})
    app.register_blueprint(movies.blueprint)
    app.register_blueprint(actors.blueprint)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def get_hello_world():
        return jsonify({
            'message': 'Hello world!'
        }), 200

    @app.route('/get-movies')
    @requires_auth(permission='get:movies')
    def get_movies():
        return jsonify({
            'message': 'Hello world! This resource requires authentication'
        }), 200


def register_errorhandlers(app):

    def errorhandler(error):
        response = error.to_json()
        response.status_code = error.status_code
        return response

    app.errorhandler(AuthError)(errorhandler)
    app.errorhandler(ResourceNotFound)(errorhandler)
    app.errorhandler(BadRequest)(errorhandler)
    app.errorhandler(InternalServerError)(errorhandler)
