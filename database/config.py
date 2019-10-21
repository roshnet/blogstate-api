from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
