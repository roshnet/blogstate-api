from api import app
from api.models import Posts
from api.models import Credentials as Creds
import json
import uuid


class FetchPostResource:
    def on_get(self, req, resp, username, url):
        user = Creds.get_or_none(Creds.username == username)

        if user:
            post = Posts.get_or_none(Posts.post_url == url)
            if post:
                resp.body = json.dumps({
                    "status": "pass",
                    "author": {
                        "name": user.name,
                        "username": user.username
                    },
                    "post": {
                        "title": post.title,
                        "body": post.body
                    }
                })
            else:
                resp.body = json.dumps({
                    "status": "fail",
                    "msg": "Post not found under specified user"
                })
        else:
            resp.body = json.dumps({
                "status": "fail",
                "msg": "No such user found"
            })


app.add_route('/{username}/post/{url}', FetchPostResource())
