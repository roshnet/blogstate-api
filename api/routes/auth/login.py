import json
from api import app

# Models for database
from api.models import Credentials

# Password hash validation
from werkzeug.security import check_password_hash as cph


class LoginResource:
    def on_post(self, req, resp):
        """
        Expected params as body of POST request:
            :param `username`
            :param `passwd` 
        """

        _creds = json.loads(req.stream.read())

        if Credentials.select().where(
          Credentials.username == _creds['username']).exists():
            rec = Credentials.get(Credentials.username == _creds['username'])
            if cph(rec.hash, _creds['passwd']):
                resp.body = json.dumps({"status": "verified"})
            """
            Above approach is failsafe, but slow, since "searching for
            username existence" and then "fetching hash for that username"
            are two different ops, and take alomst double the time.

            A better approach is to search and fetch the hash for the
            username in a single query.
            It would double speed and also reduce load on the server.
            """
        else:
            resp.body = json.dumps({"status": "unauthorised"})


app.add_route('/login', LoginResource())
