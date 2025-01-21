from sqlalchemy import String, Integer, Column, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
#     posts = relationship('Post', back_populates='author')

# class Post(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(200), nullable=False)
#     content = Column(Text, nullable=False)
#     author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     author = relationship('User', back_populates='posts')