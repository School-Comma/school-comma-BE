from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError
from repository.user_repository import UserRepository
from database.models import User
from utils.auth import Crypto, JWT
import os
from dotenv import load_dotenv

# reuseable_oauth = OAuth2PasswordBearer(
#     tokenUrl='/login',
#     scheme_name='JWT'
# )
load_dotenv()

class UserService:
    def __init__(self, user_repo : UserRepository = Depends()   , 
                 crypto : Crypto = Depends(), 
                 jwt : JWT = Depends()
                 ):
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
        access_token = self.jwt.create_access_token(data={'sub':user.email})
        refresh_token = self.jwt.create_refresh_token(data={'sub':user.email})
        return {
            "access_token": access_token,
            "refresh_token": refresh_token 
        }
        
        
        
def get_current_user(token: str, user_repo : UserRepository = Depends()):
        try:
            payload = jwt.decode(
                token, os.getenv("secret_key"), algorithms=[os.getenv("algorithm")]
            )
            email = payload.get('sub')
            if email is None:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='토큰이 유효하지 않습니다.',
                )
            user = user_repo.find_by_email(email=email)
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='사용자를 찾을 수 없습니다.'
                )
            return user
        except ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='토큰이 만료되었습니다.',
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail='자격 증명을 확인할 수 없습니다.',
            )