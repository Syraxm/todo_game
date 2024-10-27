from . import db

# todo: accounts system
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.Text, nullable=False)
#     health = db.Column(db.Integer, nullable=False, default=50)
#     manna = db.Column(db.Integer, nullable=False, default=50)
#     points = db.Column(db.Integer, nullable=False, default=0)
#     level = db.Column(db.Integer, nullable=False, default=0)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.Text, nullable=False)
    complete = db.Column(db.Boolean)
