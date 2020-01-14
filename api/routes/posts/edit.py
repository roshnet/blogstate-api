from api import app
from api.models import Posts
from api.models import Credentials as Creds
import falcon
import json


class UpdatePostResource:
    """Like CreatePostResource(), performs an UPDATE instead."""
    def on_put(self, req, resp):
        username = req.params.get('a')
        post_idf = req.params.get('p')
        if username and post_idf:
            try:
                _ = (Posts
                    .update(
                        body=req.media.get('body'),
                        title=req.media.get('title'),
                        preview_text=req.media.get('preview_text')
                    ).where(
                        (Posts.post_url == post_idf)
                    )).execute()
                """
                NOTE: Above logic can give false positives, as the
                where() clause does not throw exceptions if a record
                matching the condition is not found.
                Alter logic to:
                    - check if `post_idf` exists under `author` username
                    - apply update using record only if it exists.
                This won't give any false positives as `.where()` will
                only hold a record that exists.
                """
                # On successful UPDATE #
                resp.body = json.dumps({
                    "status": "pass"
                })
            except:
                resp.body = json.dumps({
                    "status": "fail"
                })
        else:
            raise falcon.HTTPBadRequest(description="Insufficient arguments")


app.add_route('/posts/edit/', UpdatePostResource())
# Expects two query parameters: `a` and `p` for `author`
# and `post_idf` respectively.
