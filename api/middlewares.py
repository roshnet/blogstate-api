# All falcon middlewares #

from api.models import db
from dotenv import load_dotenv
import falcon
import os

load_dotenv()


class PeeweeConnectionMiddleware(object):
    # :- Middleware for peewee reconnection -: #

    def process_request(self, req, resp):
        if db.is_closed():
            db.connect()


class SourceVerifierMiddleware(object):
    """
    Check if the agent calling the API is a trusted source,
    by checking the authorization token in request headers.
    """
    def process_request(self, req, resp):
        if not self._load_token_and_validate(req):
            raise falcon.HTTPUnauthorized('No authorization token found'
                                          'in request.')

    def _load_token_and_validate(self, req):
        self.KEY = os.getenv('AUTH')

        if req.get_header('Authorization') == self.KEY:
            return True
        return False
