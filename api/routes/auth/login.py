from api import app
from database.workers import record_exists


class LoginResource:

    def on_get(self, req, resp):
        username = req.params.get('user')
        out = record_exists(tbl_name='credentials', username=username, name='')
        print(out)
        resp.media = out

    def on_post(self, req, resp):
        resp.media = f"/login"


app.add_route('/login', LoginResource())
