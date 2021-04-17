from flask import Flask, request, abort, jsonify
from flask_cors import CORS

from .models import setup_db


def create_app(config='casting_agency.config'):
    app = Flask(__name__)
    app.config.from_object(config)

    db = setup_db(app)

    # Set up CORS. Allow '*' for origins
    CORS(app, resources={r"/*": {"origins": "*"}})

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
    
    return app
