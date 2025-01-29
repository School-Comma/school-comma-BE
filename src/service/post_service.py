from fastapi import Depends, HTTPException
from repository.post_repository import PostRepository
from database.models import Post

class PostService:
    def __init__(self, post_repo : PostRepository = Depends()):
        self.post_repo = post_repo
    
    def create_post(self, title:str, content:str, author_id:int):
        post = Post(title=title, content=content, author_id=author_id)
        self.post_repo.save(post=post)
        return post
    