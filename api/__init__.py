import falcon
from api.middlewares import (
    PeeweeConnectionMiddleware,
    SourceVerifierMiddleware
)


app = falcon.API(middleware=[
        PeeweeConnectionMiddleware(),
        SourceVerifierMiddleware()
    ]
)

import api.routes    # noqa
