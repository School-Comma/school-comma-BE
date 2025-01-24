from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from repository.user_repository import UserRepository
from database.models import User
from utils.auth import Crypto, JWT

class UserService:
    def __init__(self, user_repo : UserRepository = Depends(), crypto : Crypto = Depends(), jwt : JWT = Depends()):
        self.user_repo = user_repo
        self.crypto = crypto
        self.jwt = jwt
    
    def register_user(self, username : str, email : str, password : str):
        if len(username) > 20:
            raise HTTPException(status_code=400, detail='20글자 내외로 작성해주세요!')
        if self.user_repo.find_by_email(email=email):
            raise HTTPException(status_code=400, detail='이미 있는 이메일 입니다!')
        hashed_password = self.crypto.hash_password(password=password)
        user = User(username=username, password=hashed_password, email=email)
        self.user_repo.save(user)
        return user

    def login_user(self, email : str, password : str):
        user = self.user_repo.find_by_email(email=email)
        if not user or not self.crypto.verify_password(plain_password=password, hashed_password=user.password):
            raise HTTPException(status_code=401, detail='이메일 혹은 비밀번호가 잘못 되었습니다!')
        access_token = self.jwt.JWTEncoder(data={'sub':user.email})
        return access_token