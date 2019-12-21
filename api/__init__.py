import falcon
from api.middlewares import (
    PeeweeConnectionMiddleware,
    AuthorizationMiddleware
)


app = falcon.API(middleware=[
        PeeweeConnectionMiddleware(),
        AuthorizationMiddleware()
    ]
)

import api.routes    # noqa
