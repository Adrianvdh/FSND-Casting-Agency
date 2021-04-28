from flask import Flask, jsonify

from .extensions import db, migrate, cors
from .auth import requires_auth
from .config import DefaultConfig


def create_app(config_object=DefaultConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    register_extensions(app)
    register_views(app)

    return app


def register_extensions(app):
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)


def register_views(app):
    # Set up CORS. Allow '*' for origins
    cors.init_app(app, resources={r"/*": {"origins": "*"}})

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
    def get_movies(jwt):
        return jsonify({
            'message': 'Hello world! This resource requires authentication'
        }), 200
