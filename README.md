# FSND Casting Agency API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

This project has a few key dependencies.

#### The Web Framework:
- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

#### The ORM (database) Layer:
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) is an extension for Flask that adds support for SQLAlchemy to your application.
- [Flask-Migrate](flask-migrate.readthedocs.io/) is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.

#### The API Layer:
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Developer environment setup

## Environment Vars Setup
Please create a development and test environment source files from the `.env-template` file. This
will ensure the application has the correct configuration to run in development mode and to run the tests.

```bash
# .env
export DB_USER=DB_USER_HERE
export DB_HOST=DB_HOST_HERE
export DB_POST=DB_PORT_HERE
export DB_NAME=DB_NAME_HERE
```

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
# createdb udacity_casting_agency # TODO
# psql udacity_trivia < casting_agency.psql # TODO 
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source .env
export FLASK_APP=casting_agency
export FLASK_ENV=development
pip install -e .
flask db upgrade
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `casting_agency` directs flask to use the `casting_agency` directory and the `__init__.py` file to find the application. 

## Flask-Migrate:
For documentation purposes for the developer:

Create the migration repository (This is only done once - and is already done):
```bash
$ flask db init
```

Create a migration. Make some changes to the `models.py` class models, and then make migrations:
```bash
$ flask db migrate -m "Initial migration."
```

Apply the newly created migration scripts to migrate your database:
```bash
$ flask db upgrade
```

## Testing
To run the automated tests, run
```
pytest
```

# API Documentation
## Getting Started
- The backend app is hosted at http://127.0.0.1:5000/
- Authentication: This application does not require authentication.


## Error Handling
Errors are returned as JSON objects in the following format;

```json
{
    "success": false,
    "error": "500 Internal Server Error",
    "message": "Bad request!"
}
```

The API will return three error types when a request fails:
- 400 Bad Request
- 404 Not Found
- 405 Method Not Allowed
- 422 Unprocessable
- 500 Internal Server Error

## Endpoints

...
