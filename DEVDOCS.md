
### Adding a new endpoint

Every endpoint has it's code in a module in the `routes/` directory. 

Let's say you call the module `endpoint.py`, and it is meant to introduce the
endpoint `/newendpoint`. Let the corresponsing Falcon class  be `NewResource()`. 

The new module `endpoint.py` should have the following structure:

```py

from api import app


class NewResource():
    # Handler methods for requests.
    # Definitions for `on_get`, `on_put`, etc.


app.add_route('/<new_endpoint>', NewResource())

```
... where `api` is the project name.

After this is done, edit the `routes/__init__.py` file to include this `NewResource()` as well:

```py
# Existing imports
import api.routes.endpoint

```