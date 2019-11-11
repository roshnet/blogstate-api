from api import app
from api.models import Posts
from api.models import Credentials as Creds
import json
import uuid


class FetchPostResource:
    def on_get(self, req, resp, username, url):

        post = Posts.get_or_none(Posts.post_url == url)
        if not post is None:
            user = Creds.get_or_none(Creds.user_id == post.author_uid)
            if not user is None:
                if user.username == username:
                    resp.body = json.dumps({
                        "status": "pass",
                        "author": {
                            "name": user.name,
                            "username": user.username
                        },
                        "post": {
                            "title": post.title,
                            "body": post.body,
                            "date": str(post.time)
                        }
                    })
                else:
                    resp.body = json.dumps({
                        "status": "fail",
                        "msg": "Username in URL does not match author"
                    })
            else:
                resp.body = json.dumps({
                    "status": "fail",
                    "msg": "No author found for this blog post"
                })
        else:
            resp.body = json.dumps({
                "status": "fail",
                "msg": "No blog post found"
            })


app.add_route('/{username}/post/{url}', FetchPostResource())
