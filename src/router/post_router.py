from fastapi import APIRouter, Depends
from router.schema.post_schema import PostCreate
from service.post_service import PostService
from service.user_service import get_current_user

router = APIRouter()

@router.post('/post')
def create_post(request : PostCreate, post_service : PostService = Depends(), current_user : get_current_user = Depends()):
    post = post_service.create_post(title=request.title, content=request.content, author_id=current_user.id)
    return {
        'id' : current_user.id,
        'title' : request.title,
        'content' : request.content,
        'author' : current_user.username,
        'author_id' : post.id
    }