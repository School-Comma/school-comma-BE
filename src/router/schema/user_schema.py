from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    username : str
    email : EmailStr
    password : str

class LoginUser(BaseModel):
    email : EmailStr
    password : str


