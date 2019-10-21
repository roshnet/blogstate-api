"""
Helper classes and functions for database interactions.
"""
from database.config import (
    host,
    user,
    password
)
import pymysql


db = 'blogstate'
conn = pymysql.connect(host, user, password, db)
cur = conn.cursor()
