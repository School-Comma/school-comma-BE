from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)
SessionFactory = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()