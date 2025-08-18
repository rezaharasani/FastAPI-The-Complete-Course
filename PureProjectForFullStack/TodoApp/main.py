from fastapi import FastAPI
from TodoApp import models
from TodoApp.database import engine
from TodoApp.routers import auth, todos

from starlette.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")

app.include_router(auth.router)
app.include_router(todos.router)
