from api import app
from api.models import Posts
from api.models import Credentials as Creds
import json


class FetchPostResource:
    """Fetch a single post described by username and post ID"""
    def on_get(self, req, resp, username, idf):
        post = Posts.get_or_none(Posts.post_url == idf)
        if post is not None:
            user = Creds.get_or_none(Creds.user_id == post.author_uid)
            if user is not None:
                if user.username == username:
                    resp.body = json.dumps({
                        "status": "pass",
                        "result": {
                            "post_id": post.get_id(),
                            "title": post.title,
                            "body": post.body,
                            "preview_text": post.preview_text,
                            "idf": idf,
                            "date": str(post.time),
                            "author": {
                                "name": user.name,
                                "username": user.username
                            },
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
                    "msg": "Cannot find the author of this blog post"
                })
        else:
            resp.body = json.dumps({
                "status": "fail",
                "msg": "No blog post found"
            })


app.add_route('/posts/{username}/{idf}', FetchPostResource())
