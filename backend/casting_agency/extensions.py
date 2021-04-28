from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


# Bind the flask application and a SQLAlchemy ORM:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#configuration
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
# https://flask-migrate.readthedocs.io/en/latest/#command-reference

db = SQLAlchemy(session_options={
    'expire_on_commit': False
})

migrate = Migrate()
cors = CORS()

