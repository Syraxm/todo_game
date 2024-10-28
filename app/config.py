import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///todo_game.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
