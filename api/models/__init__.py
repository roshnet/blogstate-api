from database import HOST, USER, PASSWD
import datetime
import peewee as pw

db = pw.MySQLDatabase('blogstate',
                      user=USER,
                      password=PASSWD,
                      host=HOST)


# -: Base model to set database :- #

class BaseModel(pw.Model):
    class Meta:
        database = db


class Credentials(BaseModel):
    user_id = pw.IntegerField(primary_key=True)
    username = pw.CharField()
    hash = pw.CharField()
    email = pw.CharField()
    name = pw.CharField()

    class Meta:
        db_table = 'credentials'


class Posts(BaseModel):
    post_id = pw.IntegerField(primary_key=True)
    author_uid = pw.CharField()
    title = pw.CharField()
    body = pw.TextField()
    likes = pw.IntegerField()
    time = datetime.datetime.now

    class Meta:
        db_table = 'posts'
