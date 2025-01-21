from fastapi import APIRouter, Depends
from service.user_service import UserService
from router.schema.user_schema import CreateUser

router = APIRouter(prefix='/user')


@router.post('/signup')
def signup(request : CreateUser, user_service : UserService = Depends()):
    user = user_service.register_user(username=request.username, email=request.email, password=request.password)
    return {"id" : user.id, "username" : user.username, "email" : user.email}