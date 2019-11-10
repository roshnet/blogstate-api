from api import app
from api.models import Posts
from api.models import Credentials as Creds
import json


class FetchPostsByUserResource:
    def on_get(self, req, resp, username):
        user = Creds.get_or_none(Creds.username == username)
        if user is not None:
            posts = Posts.select().where(
                Posts.author_uid == user.get_id()
            ).dicts()

            # Create a payload out of query results
            payload = []
            for post in posts:
                payload.append({
                    "id": post['post_id'],
                    "url_id": post['post_url'],
                    "title": post['title'],
                    "body": post['body']
                })
            # Not sending author username in response,
            # as it is already specified/known by the calling agent.

            resp.body = json.dumps({
                "status": "pass",
                "posts": payload,
                "count": len(posts)
            })
        else:
            resp.body = json.dumps({
                "status": "fail"
            })


app.add_route('/posts/{username}', FetchPostsByUserResource())
