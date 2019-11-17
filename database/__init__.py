import inspect
import os

ENV_FILENAME = '.env'

# Switching to reading static file, since loading environment
# variables causes nuisance in production server.

this_module = inspect.getfile(inspect.currentframe())
this_dir = os.path.dirname(this_module)
envfile_path = os.path.join(this_dir, ENV_FILENAME)

with open(envfile_path) as fp:
    HOST = fp.readline().rstrip("\n")
    USER = fp.readline().rstrip("\n")
    PASSWD = fp.readline().rstrip("\n")
    DATABASE = fp.readline().rstrip("\n")
