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
    
    def list_get_post(self):
        return self.post_repo.find_all()
    
    def get_post(self, post_id:int):
        post = self.post_repo.find_by_id(post_id=post_id)
        if post is None:
            raise HTTPException(status_code=404, detail='찾으시는 게시물은 존재하지 않습니다.')
        return post
    
    def update_post(self, post_id : int, title:str, content:str, author_id:int):
        post = self.get_post(post_id=post_id)
        if post.author_id != author_id:
            raise HTTPException(status_code=403, detail='수정할 권한이 없습니다.')
        post.title = title
        post.content = content
        self.post_repo.save(post=post)
        return post