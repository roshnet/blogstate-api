from api import app
from api.models import Posts
import json
import uuid


class CreatePostResource:
    def on_post(self, req, resp):
        _fields = json.loads(req.stream.read())

        try:
            Posts.create(
                author_uid=_fields['author_uid'],
                post_url=uuid.uuid4().hex,
                title=_fields['title'],
                body=_fields['body'],
            )
            resp.body = json.dumps({
                "status": "pass"
            })
        except Exception as err:
            resp.body = json.dumps({
                "status": "fail",
                "error": err
            })


app.add_route('/posts/new', CreatePostResource())
