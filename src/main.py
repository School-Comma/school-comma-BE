from fastapi import FastAPI
from src.router import user_router, post_router
from src.database.connection import engine
import src.database.models

src.database.models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router.router)
app.include_router(post_router.router)


@app.get('/')
def hello():
    return 'hello'