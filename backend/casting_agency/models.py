from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(session_options={
    'expire_on_commit': False
})


def setup_db(app):
    """
    Bind the flask application and a SQLAlchemy ORM:
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#configuration
    https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application
    https://flask-migrate.readthedocs.io/en/latest/#command-reference
    """

    db.init_app(app)

    # initializes the extension with the standard Flask command-line interface:
    migrate = Migrate(app, db)
    return db