from sqlalchemy.schema import CreateTable
from src.database.models import User, Post
from src.database.connection import engine

print(CreateTable(Post.__table__).compile(engine))

# import secrets

# # 시크릿 키 생성
# secret_key = secrets.token_hex(32)  # 32바이트 길이의 시크릿 키 생성
# print(secret_key)
