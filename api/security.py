# Implement security related functions #

from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv('API_KEY')


def verify_source(req):
    headers = req.headers

    print(headers)

    if headers['API-KEY'] == KEY:
        print("Trusted source")
    else:
        print("Do not trust")
