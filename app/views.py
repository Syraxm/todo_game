from flask import Blueprint, render_template
from .models import Todo
from . import db

main = Blueprint('main', __name__)

@main.route('/home_page')
def home():
    todo_list = Todo.query.all()
    return render_template('home.html', todo_list=todo_list)
