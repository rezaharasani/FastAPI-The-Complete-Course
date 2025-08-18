from fastapi import FastAPI, status
from starlette.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from TodoApp import models
from TodoApp.database import engine
from TodoApp.routers import auth, todos, users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")


@app.get("/")
async def root():
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
