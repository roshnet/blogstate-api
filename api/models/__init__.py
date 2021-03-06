from api.middlewares import db
import datetime
import peewee as pw


# -: Base model to set database :- #

class BaseModel(pw.Model):
    class Meta:
        database = db


class Credentials(BaseModel):
    user_id = pw.AutoField()
    username = pw.CharField()
    hash = pw.CharField()
    email = pw.CharField()
    name = pw.CharField()

    class Meta:
        db_table = 'credentials'


class Posts(BaseModel):
    post_id = pw.AutoField()
    author_uid = pw.CharField()
    post_url = pw.CharField()
    title = pw.CharField()
    body = pw.TextField()
    preview_text = pw.CharField()
    likes = pw.IntegerField(default=0)
    time = pw.DateField(default=datetime.datetime.now)

    class Meta:
        db_table = 'posts'


class Comments(BaseModel):
    comment_id = pw.AutoField()
    author_uid = pw.IntegerField()
    post_uid = pw.IntegerField()
    body = pw.TextField()
    time = pw.DateField(default=datetime.datetime.now)

    class Meta:
        db_table = 'comments'
