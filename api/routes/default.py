from api import app


class DefaultResource:
    def on_get(self, req, resp):
        resp.body = "HTTP 200"


app.add_route('/', DefaultResource())
