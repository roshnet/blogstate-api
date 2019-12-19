from api import app
from api.models import Credentials as Creds
from api.models import Posts
import json


class FetchUserInfoResource:
    """Return all (template-) usable information for a specified user"""
    def on_get(self, req, resp, username):
        user = Creds.get_or_none(Creds.username == username)
        if user is not None:
            posts_by_user = Posts.select().where(
                Posts.author_uid == user.get_id()
            ).dicts()

            # Specify all fields here to be used in templates
            resp.body = json.dumps({
                "status": "pass",
                "result": {
                    "user_id": user.get_id(),
                    "username": user.username,
                    "name": user.name,
                    "email": user.email,
                    "stats": {
                        "posts_count": len(posts_by_user)
                    }
                }
            })
            # Include fields like followers/following count in
            # future versions
        else:
            resp.body = json.dumps({
                "status": "fail"
            })


app.add_route('/users/{username}', FetchUserInfoResource())
