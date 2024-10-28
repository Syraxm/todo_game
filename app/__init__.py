from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='static')
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import models
        from .views import register_routes

        db.create_all()
        register_routes(app)


    return app
