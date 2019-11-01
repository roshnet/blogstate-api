import json
from api import app

# Models for database
from api.models import Credentials as Creds

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

        record = Creds.get_or_none(Creds.username == _creds['username'])
        if record:
            if cph(record.hash, _creds['passwd']):
                resp.body = json.dumps({"status": "pass"})
            else:
                resp.body = json.dumps({
                    "status": "fail",
                    "msg": "Incorrect password"
                })
        else:
            resp.body = json.dumps({
                "status": "fail",
                "msg": "Username not found"
            })


app.add_route('/login', LoginResource())
