from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template('home.html', todo_list=todo_list)


@main.route('/add_todo')
def add_todo():
    todo_title = request.args.get('todo_title')
    new_todo = Todo(title=todo_title, complete=False)

    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.home'))


def register_routes(app):
    app.register_blueprint(main)
