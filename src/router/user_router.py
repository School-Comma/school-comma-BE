from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from service.user_service import UserService
from router.schema.user_schema import CreateUser, LoginUser

router = APIRouter(prefix='/user')


@router.post('/signup')
def signup(request : CreateUser, user_service : UserService = Depends()):
    user = user_service.register_user(username=request.username, email=request.email, password=request.password)
    return {"id" : user.id, "username" : user.username, "email" : user.email}

@router.post('login')
def login(request:LoginUser, user_service : UserService = Depends()):
    token = user_service.login_user(email=request.email, password=request.password)
    return {'access_token':token, 'token_type':'bearer'}