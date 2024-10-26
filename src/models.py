import sqlalchemy as db
from sqlalchemy import Column, Integer, Text, select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = db.create_engine('sqlite:///todo_game.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(Text, nullable=False)
    health = Column(Integer, nullable=False, default=50)
    manna = Column(Integer, nullable=False, default=50)
    points = Column(Integer, nullable=False, default=0)
    level = Column(Integer, nullable=False, default=0)


Base.metadata.create_all(engine)
