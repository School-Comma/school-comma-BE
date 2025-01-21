from fastapi import Depends, HTTPException
from repository.user_repository import UserRepository
from database.models import User
from utils.auth import Crypto

class UserService:
    def __init__(self, user_repo : UserRepository = Depends(), crypto : Crypto = Depends()):
        self.user_repo = user_repo
        self.crypto = crypto
    
    def register_user(self, username : str, email : str, password : str):
        if len(username) > 20:
            raise HTTPException(status_code=400, detail='20글자 내외로 작성해주세요!')
        if self.user_repo.find_by_email(email=email):
            raise HTTPException(status_code=400, detail='이미 있는 이메일 입니다!')
        hashed_password = self.crypto.hash_password(password=password)
        user = User(username=username, password=hashed_password, email=email)
        self.user_repo.save(user)
        return user
