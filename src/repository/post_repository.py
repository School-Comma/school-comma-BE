from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.connection import get_db
from database.models import Post

class PostRepository:
    def __init__(self, session : Session = Depends(get_db)):
        self.session = session
    
    def save(self, post : Post):
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post

    def find_all(self):
        return list(self.session.scalars(select(Post)))
    
    def find_by_id(self, post_id:int) -> Post|None:
        return self.session.scalar(select(Post).where(Post.id == post_id))