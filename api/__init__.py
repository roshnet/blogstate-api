import falcon
from api.models import PeeweeConnectionMiddleware


app = falcon.API(
    middleware=[
        PeeweeConnectionMiddleware()
    ]
)

import api.routes
