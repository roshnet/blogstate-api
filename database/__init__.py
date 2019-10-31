from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv('BS_DB_USER') or ''
PASSWD = os.getenv('BS_DB_PASSWORD') or ''
HOST = os.getenv('BS_DB_HOST') or 'localhost'
