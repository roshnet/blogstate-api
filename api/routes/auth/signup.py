from api import app
import json

# Models for database
from api.models import Credentials as Creds

# Password hash generation
from werkzeug.security import generate_password_hash as gph


class SignupResource:
    def on_post(self, req, resp):
        """
        Expected params in POST body:
            :param `username`
            :param `passwd`
            :param `email`
            :param `name`
        """
        _info = json.loads(req.stream.read())

        # TODO: Test structure of incoming request body/params.

        # Check username availability
        if Creds.select().where(
          Creds.username == _info['username']).exists():
            resp.body = json.dumps({
                "status": "fail",
                "msg": "Username not available"
            })
        else:
            # Proceed with insertion
            Creds.create(
                username=_info['username'],
                hash=gph(_info['passwd'], method='sha1'),
                email=_info['email'],
                name=_info['name']
            )
            # Get id of last insertion and pass in response
            ins_id = Creds.select().order_by(Creds.user_id.desc()).get()
            resp.body = json.dumps({
                "status": "pass",
                "user_id": ins_id.user_id
            })


app.add_route('/signup', SignupResource())
