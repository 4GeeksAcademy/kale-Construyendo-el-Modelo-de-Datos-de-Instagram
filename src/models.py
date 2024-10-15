import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Followers(Base):
    __tablename__ = 'Follower'
    user_from_id = Column(Integer, ForeignKey('User.ID'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('User.ID'), primary_key=True)
    
    
class Users(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250),  unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)

class Posts(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.ID'))
    Users = relationship(Users)

class Comments(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('Post.ID'))
    author_id = Column(Integer, ForeignKey('User.ID'))
    Posts = relationship(Posts)
    Users = relationship(Users)

class Medias(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.ID'))
    Posts = relationship(Posts)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
