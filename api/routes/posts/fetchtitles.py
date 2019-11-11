from api import app
from api.models import Posts
from api.models import Credentials as Creds
import json


class FetchTitlesResource:
    """Return title and dates of all posts written by user"""
    def on_get(self, req, resp, username):
        user = Creds.get_or_none(Creds.username == username)
        if user is not None:
            posts = Posts.select().where(
                Posts.author_uid == user.get_id()
            ).order_by(Posts.post_id.desc()).dicts()

            # Create a payload for post titles
            payload = []
            for post in posts:
                payload.append({
                    "date": str(post['time']),
                    "title": post['title'],
                    "url": post['post_url']
                })
            resp.body = json.dumps({
                "status": "pass",
                "titles": payload,
                "count": len(posts)
            })
        else:
            resp.body = json.dumps({
                "status": "fail"
            })


app.add_route('/posts/titles/{username}', FetchTitlesResource())
