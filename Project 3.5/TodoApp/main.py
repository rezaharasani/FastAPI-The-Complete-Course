from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from . import models
from .database import engine
from .routers import auth, todos, admin, users, address

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(address.router)


@app.get("/")
def root_page():
    return RedirectResponse(
        url="/docs",
        status_code=status.HTTP_302_FOUND,
        headers={"Location": "/"}
    )
