from fastapi import APIRouter, Depends
from src.service.user_service import UserService, get_current_user
from src.router.schema.user_schema import CreateUser, LoginUser

router = APIRouter()


@router.post('/signup')
def signup(request : CreateUser, user_service : UserService = Depends()):
    user = user_service.register_user(username=request.username, email=request.email, password=request.password)
    return {"id" : user.id, "username" : user.username, "email" : user.email}

@router.post('/login')
def login(request:LoginUser, user_service : UserService = Depends()):
    token = user_service.login_user(email=request.email, password=request.password)
    return token

@router.get('/profile')
async def get_profile(current_user : get_current_user = Depends()):
    return {"username": current_user.username, "email": current_user.email}