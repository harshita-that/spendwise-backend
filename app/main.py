from fastapi import FastAPI
from .routers import users, expenses
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(expenses.router)