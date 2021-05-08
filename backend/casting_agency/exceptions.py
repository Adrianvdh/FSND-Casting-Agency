from flask import jsonify


class BaseException(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify(rv)


class AuthError(BaseException):
    """ A standardized way to communicate auth failure modes. """
    pass


class ResourceNotFound(BaseException):
    """ A standardized way to communicate when a resource is not found. """
    pass
