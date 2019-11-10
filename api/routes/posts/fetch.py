from api import app
from api.models import Posts
from api.models import Credentials as Creds
import json
import uuid


class FetchPostResource:
    def on_get(self, req, resp, url):
        post = Posts.get_or_none(Posts.post_url == url)
        if post:
            user = Creds.get(Creds.user_id == post.author_uid)
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
                "status": "fail"
            })

app.add_route('/posts/{url}', FetchPostResource())
