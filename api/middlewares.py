# All falcon middlewares #

from api.models import db
from dotenv import load_dotenv
import falcon
import os

load_dotenv()

KEY = os.getenv('API_KEY')


class PeeweeConnectionMiddleware(object):
    # :- Middleware for peewee reconnection -: #

    def process_request(self, req, resp):
        if db.is_closed():
            db.connect()


class SourceVerifierMiddleware(object):
    """
    Check if the agent calling the API is a trusted source,
    by checking the API key in request headers.
    """
    def process_request(self, req, resp):
        if 'API-KEY' in req.headers.keys():
            if not req.headers['API-KEY'] == KEY:
                raise falcon.HTTPBadRequest('Untrusted Source',
                                            'Agent unauthorised')
        else:
            raise falcon.HTTPBadRequest('Untrusted Source',
                                        'Agent unauthorised')
