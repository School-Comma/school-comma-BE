from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import User

class UserRepository:
    def __init__(self, session : Session = Depends(get_db)):
        self.session = session
    
    def save(self, user : User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def find_by_email(self, email : str)-> User | None:
        return self.session.scalar(select(User).where(User.email == email))
