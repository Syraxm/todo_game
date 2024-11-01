from . import db

# todo: accounts system
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.Text, nullable=False)
    points = db.Column(db.Integer, nullable=False, default=0)
    level = db.Column(db.Integer, nullable=False, default=0)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.Text, nullable=False)
    complete = db.Column(db.Boolean)
    level = db.Column(db.Integer)
