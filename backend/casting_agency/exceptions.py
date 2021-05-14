from flask import jsonify


class APIException(Exception):
    error = 'Internal Server Error'
    status_code = 500

    def __init__(self, message, error=None, status_code=None):
        Exception.__init__(self)
        self.message = message
        if error:
            self.error = error
        if status_code:
            self.status_code = status_code

    def to_json(self):
        return jsonify({
            'success': False,
            'error': self.error,
            'message': self.message
        })


class AuthError(APIException):
    """ A standardized way to communicate auth failure modes. """
    pass


class ResourceNotFound(APIException):
    error = 'Resource Not Found'
    status_code = 404


class BadRequest(APIException):
    error = 'Bad Request'
    status_code = 400


class InternalServerError(APIException):
    error = 'Internal Server Error'
    status_code = 500
