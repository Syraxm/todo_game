from flask import Blueprint, render_template
from .models import Todo
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template('home.html')


def register_routes(app):
    app.register_blueprint(main)
