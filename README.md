# FSND Casting Agency Project

A live demo of the application is available at:
[https://fsnd-casting-agency.netlify.app](https://fsnd-casting-agency.netlify.app)

*Please refer to the [Authentication section](#authentication) for login details*

## Content
1. [Motivation for the project](#project-motivation)
2. [Project setup and dependencies](#project-setup)
2. [API documentation](#api-documentation)
2. [Authentication](#authentication)


# <a name="project-motivation"></a>
## Motivation for the project
This project is the final project of the Udacity Full Stack Nanodegree course. It covers the following topics
1. Database modeling techniques using PostgreSQL as the database and `SQL-Alchemy` as the Python ORM (see `models.py`)
2. API development exposing the application data and enabling user operations such as creating, updating and deleting
`Actors` and `Movies` (see `app.py`, `api/movies.py`, `api/actors.py`)
3. Test-Driven development of automated tests (see `tests/`).
4. Authorization and Role-based Authentication (a.k.a RBAC) with `Auth0` (see `auth.py`).
5. Deployment of the backend application on a live `Heroku` server, and the frontend onto `Netify`.
6. BONUS: Development of a frontend application (using `React.js`) to list `Actors` and `Movies`. 


# <a name="project-setup"></a>
## Project setup and dependencies

## Backend API

### Installing Dependencies

#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

1. Create a new virtual environment by running the following command:
```bash
$ python3 -m venv venv
```
   
2. Activate your new virtual environment by running the following command:
```bash
$ source venv/bin/activate
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running the following command:

```bash
$ pip install -r requirements.txt
```

This will install all the required packages selected within the `requirements.txt` file.

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

### Developer environment setup

## Environment Vars Setup
Please create a development and test environment source files from the `.env-template` file. This
will ensure the application has the correct configuration to run in development mode and to run the tests.

```bash
# .env
export DATABASE_URL_NEW='postgresql://adrian@localhost:5432/udacity_casting_agency'
```

### Database Setup
With Postgres running, create and restore the database using the `udacity_casting_agency.dump` file provided using the following commands:
```bash
$ pg_restore -C -d postgres udacity_casting_agency.dump
```

## Running the server

To run the server, execute:

```bash
./run.sh
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
To run the automated tests please run the following commands.

1. Create a test database:
```bash
createdb udacity_casting_agency_test
```

2. Install the testing dependencies with `pip`:
```bash
$ pip install -r requirements-test.txt
```

3. Execute the automated tests by running `pytest`
```bash
pytest
```

## Frontend Application

### Installing Dependencies

#### NodeJS 12.0
Follow instructions to install the latest version of node.js for your platform in the [nodejs](https://nodejs.org/en/download/)


#### React Dependencies

Once you have your node js environment setup and running, from the `./frontend` directory install dependencies by running the following command:

```bash
$ npm install
```

This will install all the required packages selected within the `package.json` file.


## Running the frontend

To start the frontend application, execute:

```bash
npm start
```

And Bob's your uncle! You should have the full application running!!!


# <a name="api-documentation"></a>
## API Documentation
## Getting Started
Here you'll find all the API endpoints that expose the `Movies` and `Actors` data to be consumed from the frontend.

### Base URL
https://fsnd-casting-agency-adrian.herokuapp.com

### Authentication
Please refer to the [Authentication section](#authentication)

## Error Handling
Errors are returned as JSON objects in the following format;

```json
{
    "success": false,
    "error": "Resource Not Found",
    "message": "Movie could not be found!"
}
```

The API will return three error types when a request fails:
- 400 Bad Request
- 404 Not Found
- 405 Method Not Allowed
- 422 Unprocessable
- 500 Internal Server Error

## Endpoints
Here is a list of all the available endpoints and their respective HTTP method.

- Movies
    - [GET /api/movies](#get-movies)
    - [GET /api/movies/<movie_id>](#get-movie)
    - [POST /api/movies/](#post-movie)
    - [DELETE /api/movies/<movie_id>](#delete-movie)
    - [PATCH /api/movies/<movie_id>](#patch-movie)
- Actors
    - [GET /api/actors](#get-actors)
    - [GET /api/actors/<actor_id>](#get-actor)
    - [POST /api/actors/](#post-actor)
    - [DELETE /api/actors/<actor_id>](#delete-actor)
    - [PATCH /api/actors/<actor_id>](#patch-actor)


# <a name="get-movies"></a>
### GET /api/movies
Get a list of all the movies on the server.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/movies`

- Returns a list of movies along with the cast of each movie.
- Request Headers: *Authorization*
- Request permission: `get:movies`
- Response body:
  - List of dict values each representing a movie object.
    - string `cover_image_url`
    - string `description`
    - string `duration`
    - string `genre`
    - integer `id` unique identifier of the movie
    - string `release_date`
    - string `title`
    - list `cast` a list of dict values each representing an actor object.
      - string `cover_image_url`
      - string `date_of_birth`
      - string `description`
      - string `full_name`
      - string `height`
      - integer `id` unique identifier of the actor

- Actual response body:
```json
[
  {
    "cast": [
      {
        "cover_image_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRaylUHDnhsws_8SY-iV2eAnrsR9d3hAtkELLjBz9JDA_LFSN_b",
        "date_of_birth": "19 November 1961",
        "description": "Meg Ryan is an American actress and producer. Ryan began her acting career in 1981 in minor roles before joining the cast of the CBS soap opera As the World Turns in 1982.",
        "full_name": "Meg Ryan",
        "gender": "Female",
        "height": "1m 73cm",
        "id": 29
      },
      {
        "cover_image_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTC8rNntc8fBOn3susRUeFJTJDOkt_0Y30znA0BOci132r75MKy",
        "date_of_birth": "14 March 1948",
        "description": "William Edward Crystal is an American actor, comedian, writer, producer, director and television host. He gained prominence in the 1970s and 1980s for television roles as Jodie Dallas on the ABC sitcom Soap and as a cast member and frequent host of Saturday Night Live",
        "full_name": "Billy Crystal",
        "gender": "Male",
        "height": "1m 70cm",
        "id": 30
      }
    ],
    "cover_image_url": "https://m.media-amazon.com/images/M/MV5BMjE0ODEwNjM2NF5BMl5BanBnXkFtZTcwMjU2Mzg3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "description": "A chance encounter between two graduates culminates in a short-term friendship. But when fate brings them back together five years later, they are forced to deal with how they feel about each other.",
    "duration": "1h 36m",
    "genre": "Romance/Comedy",
    "id": 74,
    "release_date": "21 July 1989",
    "title": "When Harry Met Sally..."
  }
]
```

# <a name="get-movie"></a>
### GET /api/movies/<movie_id>

Get the information for a specific movie identified by the movie id.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/movies/74`

- Returns a dict representing a movie.
- Request Headers: *Authorization*
- Request permission: `get:movie-detail`
- Response body:
  - A dict representing a movie object.
    - string `cover_image_url`
    - string `description`
    - string `duration`
    - string `genre`
    - integer `id` unique identifier of the movie
    - string `release_date`
    - string `title`
    - list `cast` a list of dict values each representing an actor object.
      - string `cover_image_url`
      - string `date_of_birth`
      - string `description`
      - string `full_name`
      - string `height`
      - integer `id` unique identifier of the actor

- Actual response body:
```json
{
  "cast": [
    {
      "cover_image_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRaylUHDnhsws_8SY-iV2eAnrsR9d3hAtkELLjBz9JDA_LFSN_b",
      "date_of_birth": "19 November 1961",
      "description": "Meg Ryan is an American actress and producer. Ryan began her acting career in 1981 in minor roles before joining the cast of the CBS soap opera As the World Turns in 1982.",
      "full_name": "Meg Ryan",
      "gender": "Female",
      "height": "1m 73cm",
      "id": 29
    },
    {
      "cover_image_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTC8rNntc8fBOn3susRUeFJTJDOkt_0Y30znA0BOci132r75MKy",
      "date_of_birth": "14 March 1948",
      "description": "William Edward Crystal is an American actor, comedian, writer, producer, director and television host. He gained prominence in the 1970s and 1980s for television roles as Jodie Dallas on the ABC sitcom Soap and as a cast member and frequent host of Saturday Night Live",
      "full_name": "Billy Crystal",
      "gender": "Male",
      "height": "1m 70cm",
      "id": 30
    }
  ],
  "cover_image_url": "https://m.media-amazon.com/images/M/MV5BMjE0ODEwNjM2NF5BMl5BanBnXkFtZTcwMjU2Mzg3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
  "description": "A chance encounter between two graduates culminates in a short-term friendship. But when fate brings them back together five years later, they are forced to deal with how they feel about each other.",
  "duration": "1h 36m",
  "genre": "Romance/Comedy",
  "id": 74,
  "release_date": "21 July 1989",
  "title": "When Harry Met Sally..."
}
```

# <a name="post-movie"></a>
### POST /api/movies/

Creates a new movie using the submitted data.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/movies -X POST -H "Content-Type: application/json"
-H "Authorization: Bearer ..." -d '{"title": "Bee Movie", "description": "A movie about bees",
"genre": "Kids", "release_date": "2007-12-12", "duration": 90, "cover_image_url": "http://domain.com/bees.jpg"}'`

- Returns a dict representing success outcome and the created movie id.
- Request Headers: *Authorization*
- Request permission: `post:movies`
- Request body:
  - A dict representing new movie values.
      - string `cover_image_url`
      - string `description`
      - string `duration`
      - string `genre`
      - string `release_date`
      - string `title`
- Response body:
  - A dict representing a movie object.
      - boolean `success`
      - integer `created` unique identifier of the newly created movie

- Actual response body:
```json
{
  "success": true,
  "created": 89
}
```

# <a name="delete-movie"></a>
### DELETE /api/movies/<movie_id>

Deletes an existing movie by the movie id.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/movies/1 -X DELETE`

- Returns a dict representing success outcome and the created movie id.
- Request Headers: *Authentication*
- Request permission: `delete:movies`
- Response body:
  - A dict representing a movie object.
    - boolean `success`
    - integer `created` unique identifier of the newly created movie

- Actual response body:
```json
{
  "success": true,
  "deleted": 1
}
```

# <a name="patch-movie"></a>
### PATCH /api/movies/<movie_id>

Updates an existing movie using the submitted data.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/movies/1 -X PATCH -H "Content-Type: application/json"
-H "Authorization: Bearer ..." -d '{"title": "Bee Movie", "description": "A movie about bees",
"genre": "Kids", "release_date": "2007-12-12", "duration": 90, "cover_image_url": "http://domain.com/bees.jpg"}'`

- Returns a dict representing success outcome and the created movie id.
- Request Headers: *Authorization*
- Request permission: `post:movies`
  - Request body:
    - A dict representing new movie values.
      - string `cover_image_url`
      - string `description`
      - string `duration`
      - string `genre`
      - string `release_date`
      - string `title`
- Response body:
  - A dict representing a movie object.
    - boolean `success`
    - integer `created` unique identifier of the newly created movie

- Actual response body:
```json
{
  "success": true,
  "updated": 1
}
```

# <a name="get-actors"></a>
### GET /api/actors
Get a list of all the actors on the server.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/actors`

- Returns a list of actors along with a list of movies they are involved in.
- Request Headers: *Authorization*
- Request permission: `get:actors`
- Response body:
  - List of dict values each representing a actor object.
    - string `cover_image_url`
    - string `date_of_birth`
    - string `description`
    - string `full_name`
    - string `height`
    - integer `id` unique identifier of the actor
    - list `cast` a list of dict values each representing a movie object.
        - string `cover_image_url`
        - string `description`
        - string `duration`
        - string `genre`
        - integer `id` unique identifier of the movie
        - string `release_date`
        - string `title`

- Actual response body:
```json
[
  {
    "cover_image_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRaylUHDnhsws_8SY-iV2eAnrsR9d3hAtkELLjBz9JDA_LFSN_b",
    "date_of_birth": "19 November 1961",
    "description": "Meg Ryan is an American actress and producer. Ryan began her acting career in 1981 in minor roles before joining the cast of the CBS soap opera As the World Turns in 1982.",
    "full_name": "Meg Ryan",
    "gender": "Female",
    "height": "1m 73cm",
    "id": 29,
    "movies": [
      {
        "cover_image_url": "https://m.media-amazon.com/images/M/MV5BMjE0ODEwNjM2NF5BMl5BanBnXkFtZTcwMjU2Mzg3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
        "description": "A chance encounter between two graduates culminates in a short-term friendship. But when fate brings them back together five years later, they are forced to deal with how they feel about each other.",
        "duration": "1h 36m",
        "genre": "Romance/Comedy",
        "id": 74,
        "release_date": "21 July 1989",
        "title": "When Harry Met Sally..."
      }
  }
]
```

# <a name="get-actor"></a>
### GET /api/actors/<actor_id>

Get the information for a specific actor identified by the actor id.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/actors/29`

- Returns a dict representing an actor.
- Request Headers: *Authorization*
- Request permission: `get:actor-detail`
- Response body:
  - A dict representing a actor object.
    - string `cover_image_url`
    - string `date_of_birth`
    - string `description`
    - string `full_name`
    - string `height`
    - integer `id` unique identifier of the actor
    - list `movies` a list of dict values each representing a movie object.
      - string `cover_image_url`
      - string `description`
      - string `duration`
      - string `genre`
      - integer `id` unique identifier of the movie
      - string `release_date`
      - string `title`

- Actual response body:
```json
{
  "cover_image_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRaylUHDnhsws_8SY-iV2eAnrsR9d3hAtkELLjBz9JDA_LFSN_b",
  "date_of_birth": "19 November 1961",
  "description": "Meg Ryan is an American actress and producer. Ryan began her acting career in 1981 in minor roles before joining the cast of the CBS soap opera As the World Turns in 1982.",
  "full_name": "Meg Ryan",
  "gender": "Female",
  "height": "1m 73cm",
  "id": 29,
  "movies": [
    {
      "cover_image_url": "https://m.media-amazon.com/images/M/MV5BMjE0ODEwNjM2NF5BMl5BanBnXkFtZTcwMjU2Mzg3NA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
      "description": "A chance encounter between two graduates culminates in a short-term friendship. But when fate brings them back together five years later, they are forced to deal with how they feel about each other.",
      "duration": "1h 36m",
      "genre": "Romance/Comedy",
      "id": 74,
      "release_date": "21 July 1989",
      "title": "When Harry Met Sally..."
    },
    {
      "cover_image_url": "https://upload.wikimedia.org/wikipedia/en/e/ee/You%27ve_Got_Mail.jpg",
      "description": "The owner of a bookstore chain meets the owner of a quaint little bookshop online and they fall in love with each other. However, they are unaware that they are actually business rivals.",
      "duration": "1h 59m",
      "genre": "Romance/Comedy",
      "id": 75,
      "release_date": "18 December 1998",
      "title": "You've Got Mail"
    }
  ]
}
```
# <a name="post-actor"></a>
### POST /api/actors/

Creates a new actor using the submitted data.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/actors -X POST -H "Content-Type: application/json"
-H "Authorization: Bearer ..." -d '{"full_name": "Brad Pitt", "description": "A male actor from America",
"date_of_birth": "1963-12-18", "height": 180, "gender": "Male", "cover_image_url": "http://domain.com/brad.jpg"}'`

- Returns a dict representing success outcome and the created actor id.
- Request Headers: *Authorization*
- Request permission: `post:actors`
- Request body:
  - A dict representing new actor values.
    - string `cover_image_url`
    - string `description`
    - string `date_of_birth`
    - integer `height`
    - string `gender`
    - string `full_name`
- Response body:
  - A dict representing an actor object.
    - boolean `success`
    - integer `created` unique identifier of the newly created actor

- Actual response body:
```json
{
  "success": true,
  "created": 89
}
```

# <a name="delete-actor"></a>
### DELETE /api/actors/<actor_id>

Deletes an existing actor by the actor id.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/actors/1 -X DELETE`

- Returns a dict representing success outcome and the created actor id.
- Request Headers: *Authentication*
- Request permission: `delete:actors`
- Response body:
  - A dict representing a actor object.
    - boolean `success`
    - integer `created` unique identifier of the newly created actor

- Actual response body:
```json
{
  "success": true,
  "deleted": 1
}
```

# <a name="patch-actor"></a>
### PATCH /api/actors/<actor_id>

Updates an existing actor using the submitted data.

`$ curl https://fsnd-casting-agency-adrian.herokuapp.com/actors/1 -X PATCH -H "Content-Type: application/json"
-H "Authorization: Bearer ..." -d '{"full_name": "Brad Pitt", "description": "A male actor from America",
"date_of_birth": "1963-12-18", "height": 180, "gender": "Male", "cover_image_url": "http://domain.com/brad.jpg"}'`

- Returns a dict representing success outcome and the updated actor id.
- Request Headers: *Authorization*
- Request permission: `patch:actors`
- Request body:
  - A dict representing new actor values.
    - string `cover_image_url`
    - string `description`
    - string `date_of_birth`
    - integer `height`
    - string `gender`
    - string `full_name`
- Response body:
  - A dict representing an actor object.
    - boolean `success`
    - integer `created` unique identifier of update actor

- Actual response body:
```json
{
  "success": true,
  "updated": 1
}
```

# <a name="authentication"></a>
## Authentication

### Existing Roles
There are three roles with different permissions. Each role has certain actions they may perform. Each
role is promoted to greater responsibility allowing more permissions (actions).

1. The Casting Assistant may view actors and movies.
  - Can retrieve all actors.
    - Permission: `get:actors`.
    - Endpoint: `GET /actors`
  - Can retrieve a single actor's information
    - Permission: `get:actor-detail`
    - Endpoint: `GET /actors/<actor_id>`
  - Can retrieve all movies.
    - Permission: `get:movies`.
    - Endpoint: `GET /movies`
  - Can retrieve a single movie's information
    - Permission: `get:movie-detail`
    - Endpoint: `GET /movie/<movie_id>`

2. The Casting Director (every thing the Casting Assistant may do) as well as:
  - Can delete an actor:
    - Permission: `delete:actors`.
    - Endpoint: `DELETE /actors/<actor_id>`
  - Can update an existing actor:
    - Permission: `patch:actors`.
    - Endpoint: `PATCH /actors/<actor_id>`
  - Can update an existing movie:
    - Permission: `patch:movies`.
    - Endpoint: `DELETE /movies/<movie_id>`
  - Can create a new actor:
    - Permission: `post:actors`.
    - Endpoint: `POST /actors/<actor_id>`

3. The Executive Producer (every thing the Casting Director may do) as well as:
  - Can delete a movie:
    - Permission: `delete:movies`.
    - Endpoint: `DELETE /movies/<movie_id>`
  - Can create a new movie:
    - Permission: `post:movies`.
    - Endpoint: `POST /movies`


### Tokens
All API endpoints are protected with Auth0 permissions using a custom python decorator `@requires_auth`.

This means that you will have to include a `Authorization` header in each HTTP request to the API.
The server expects a `Bearer` JWT token as the value to the `Authorization` header.

`Authorization: Bearer token`

If you would like access to the API, I have provided three tokens each representing a user of each of the
aforementioned roles.

Casting Assistant:
`Email: casting.assistant@example.com`
`Password: Test1234`

Bearer token for the `Casting Assistant`:

```json
{
  "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpzWW9NWWU5dU82ZmJ3ZE4tSTdUVyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2FzdGluZy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBhOGI4ZWNmZjJkMTgwMDY5YjcxOTQ3IiwiYXVkIjpbImNhc3RpbmctYWdlbmN5LWFwaSIsImh0dHBzOi8vZnNuZC1jYXN0aW5nLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MjE2NzAyNDgsImV4cCI6MTYyMTc1NjY0OCwiYXpwIjoiWndZRVp6M3BmdjNIRmkxUERWdlE5amNneXdWbWRnU1QiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yLWRldGFpbCIsImdldDphY3RvcnMiLCJnZXQ6bW92aWUtZGV0YWlsIiwiZ2V0Om1vdmllcyJdfQ.bO8-o3Ch7nCSXaQIdzGnhwOBwXkxNQucRHueqzxEV-RHOvz8G7-CGcQjA5IQzZ_quCW9eHkq3rREDD5SZyPzJZMefYFOcsFc3YWhO8xN38CqsNvWM0R1tOK7Tu0ZAYaWybz-NNf0mljJfk6g9d3w1zjd6SWyUoxgwzH5DzdDsZMfXEA7CB72OSadUHU8wbvU92yUZqoNwio16el4H_xuIAmFXKyoBHA1IZbUdJBSFL1cf6_oliZK2L9HFdsqXvzOkMxrbXsauakens3RAhZwEYS3ohFpLrVMhQVYWScqrA9uNaEEciSjAfgC_VIquptzQoxYTauIhytzO4hJeI9pCg"

}
```

Casting Director:
`Email: casting.director@example.com`
`Password: Test1234`

Bearer token for the `Casting Director`:

```json
{
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpzWW9NWWU5dU82ZmJ3ZE4tSTdUVyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2FzdGluZy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBhOGI5YzlmZjJkMTgwMDY5YjcxOTgzIiwiYXVkIjpbImNhc3RpbmctYWdlbmN5LWFwaSIsImh0dHBzOi8vZnNuZC1jYXN0aW5nLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MjE2NzAzODgsImV4cCI6MTYyMTc1Njc4OCwiYXpwIjoiWndZRVp6M3BmdjNIRmkxUERWdlE5amNneXdWbWRnU1QiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3Rvci1kZXRhaWwiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllLWRldGFpbCIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.TlXqkk0ZcUYVYQTdbkjxCyfZVpMpeFIfjWFctYMDLbXtreL0NbKYCwpB4a_S83Q2eAeB_A89QsdbGqRzqQks3m5sO_kplffqTkXTfC5_oyHVAkMioxM3bjpLy63vdkIqW-vCxx82zkLs0_cLjS1XZJtdtAW9UNh0d7iS2r5KyN2zIhcWq8xXWv00gxdsBaggBSkFegtEB6aoArye48ao3BmjUxGj4W4aGU2mDSQ5WtqAnL-KY2Ua4DTJEid-KjXry7nCRrb77X0skKx1w49s0EuuXZ58WyPZc5Sl04NqKjgoCG5yxNhwreeDr47JgeXCUoV6vwa0B49HFd4E5-dTSg"
}
```

Executive Producer:
`Email: executive.producer@example.com`
`Password: Test1234`

Bearer token for the `Executive Producer`:

```json
{
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImpzWW9NWWU5dU82ZmJ3ZE4tSTdUVyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtY2FzdGluZy5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjBhOGJhMjQ3MDYwYWUwMDcwMzQ2N2Q4IiwiYXVkIjpbImNhc3RpbmctYWdlbmN5LWFwaSIsImh0dHBzOi8vZnNuZC1jYXN0aW5nLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MjE2NzA0NjgsImV4cCI6MTYyMTc1Njg2OCwiYXpwIjoiWndZRVp6M3BmdjNIRmkxUERWdlE5amNneXdWbWRnU1QiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3ItZGV0YWlsIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZS1kZXRhaWwiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.sYbSvEu-5zchgiC3WoN9vevzS_4m_bL4JC2W-DEGJKWMgroiXSbn8xJrXHNdFruVxExLQKGlFUP4fwiFGZhTACWZ30YywuJuL-v4jUzdMyFoDeKRJqGMbsDH1sJ9VMCKnAdU7xadcozXEdCE3mrboWIEbzD9uLC0AffqWytj2UJwxF6dQMttGZ3_3jPBem6RBrlmNlrFqUGNktR2rbjtlgbYoena0_N_4ElL3R2TFtn8D6x0gcXWlSe6Eu2CRm13vAOJ7NX_bhHG9TfNUZg9bfIkicOifDkKz3f8b9ItBOMDpnYseiaRdH3mUKfq3Ye3OrwW3zJEMMSStAZ44873Tw"
}
```
