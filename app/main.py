from fastapi import FastAPI

from .routers import login, users

app = FastAPI()
app.include_router(users.router, prefix="/user")
app.include_router(login.router, prefix="/login")


@app.get("/")
async def index():
    return {"message": "Hello World!"}
