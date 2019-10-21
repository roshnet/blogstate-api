from api import app


class LoginResource:
    def on_post(self, req, resp):
        resp.media = f"/login"


app.add_route('/login', LoginResource())
