from fastapi import FastAPI
from router import user_router

app = FastAPI()
app.include_router(user_router.router)


@app.get('/')
def hello():
    return 'hello'