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

        creds = json.loads(req.stream.read())
        record = Credentials.get(Credentials.username == creds['username'])

        if cph(record.hash, creds['passwd']):
            resp.body = json.dumps({"status": "verified"})
        else:
            resp.body = json.dumps({"status": "unauthorised"})


app.add_route('/login', LoginResource())
