from fastapi import HTTPException
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
import os
from dotenv import load_dotenv


class Crypto:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    
    def hash_password(self, password:str):
        return self.pwd_context.hash(password)
    def verify_password(self, plain_password : str, hashed_password : str):
        return self.pwd_context.verify(plain_password, hashed_password)


class JWT:
    def __init__(self):
        load_dotenv()
        self.secret_key = os.getenv('secret_key')
        self.refresh_secret_key = os.getenv('refresh_secret_key')
        self.algorithm = os.getenv('algorithm')
        self.access_token_expire_minutes = 30
        self.refresh_token_expire_minutes = 60*24*7
    
    def create_access_token(self, data:dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({'exp':expire})
        encode_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encode_jwt
    
    def create_refresh_token(self, data:dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({'exp':expire})
        encode_jwt = jwt.encode(to_encode, self.refresh_secret_key, algorithm=self.algorithm)
        return encode_jwt