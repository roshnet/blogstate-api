from api import app


class SignupResource:
    def on_post(self, req, resp):
        resp.media = f"/signup"


app.add_route('/signup', SignupResource())
