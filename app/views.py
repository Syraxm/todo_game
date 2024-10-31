from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo, User
from . import db

todo = Blueprint('main', __name__)


@todo.route('/')
def show_general_page():
    return render_template('general.html')


@todo.route('/home_page')
def home():
    todo_list = Todo.query.all()
    user = User.query.first()

    return render_template('home.html', todo_list=todo_list, points=user.points, level=user.level)


@todo.route('/registration_page')
def show_registration_page():
    return render_template('register.html')


@todo.route('/register')
def register():
    user_name = request.args.get('user_name')
    new_user = User(user_name=user_name)

    db.session.add(new_user)
    db.session.commit()

    return {'status': 200}


@todo.route('/add_todo')
def add_todo():
    todo_title = request.args.get('todo_title')
    todo_level = request.args.get('level')

    new_todo = Todo(title=todo_title, complete=False, level=todo_level)

    db.session.add(new_todo)
    db.session.commit()

    return {'status': 200}


@todo.route('/delete_todo/<todo_id>')
def delete_todo(todo_id: int):
    todo = Todo.query.filter_by(id = todo_id).first()

    db.session.delete(todo)
    db.session.commit()

    return {'status': 200}


@todo.route('/complete_todo/<todo_id>')
def complete_todo(todo_id: int):
    todo_level = request.args.get('level')

    todo = Todo.query.filter_by(id = todo_id).first()
    user = User.query.first()

    user.points += 10 * int(todo_level)
    if user.points % 50 == 0:
        user.level += 1

    db.session.delete(todo)
    db.session.commit()

    return {'status': 200}


def register_routes(app):
    app.register_blueprint(todo)
