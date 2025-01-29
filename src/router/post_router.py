from typing import List
from fastapi import APIRouter, Depends
from router.schema.post_schema import PostCreate, PostResponse
from service.post_service import PostService
from service.user_service import get_current_user

router = APIRouter()

@router.post('/post')
def create_post(request : PostCreate, post_service : PostService = Depends(), current_user : get_current_user = Depends()):
    post = post_service.create_post(title=request.title, content=request.content, author_id=current_user.id)
    return {
        'id' : post.id,
        'title' : request.title,
        'content' : request.content,
        'author' : current_user.username,
        'author_id' : current_user.id
    }

@router.get('/post', response_model=List[PostResponse])
def list_post(post_service : PostService = Depends(), current_user : get_current_user = Depends()):
    post = post_service.list_get_post()
    return post

@router.get('/post/{post_id}')
def get_post(post_id : int, post_service : PostService = Depends(), current_user : get_current_user = Depends()):
    post = post_service.get_post(post_id=post_id)
    return {
        'id' : post.id,
        'title' : post.title,
        'content' : post.content,
        'author' : current_user.username,
        'author_id' : current_user.id
    }
    
@router.patch('/post/{post_id}')
def update_post(post_id : int,request : PostCreate, post_service : PostService = Depends(), current_user : get_current_user = Depends()):
    post = post_service.update_post(post_id=post_id, author_id=current_user.id, title=request.title, content=request.title)
    return {
        'id' : post.id,
        'title' : post.title,
        'content' : post.content,
        'author' : current_user.username,
        'author_id' : current_user.id
    }

@router.delete('/post/{post_id}')
def delete_post(post_id : int, post_service : PostService = Depends(), current_user : get_current_user = Depends()):
    post = post_service.delete_post(post_id=post_id, author_id=current_user.id)
    return {'삭제가 되었습니다.'}
    