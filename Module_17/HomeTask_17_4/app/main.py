# ДДомашнее задание по теме "Использование БД в маршрутизации. 1.1"
# Задача "Маршрутизация пользователя"

from fastapi import FastAPI
from .routers import user
from .routers import task

app = FastAPI()

@app.get("/")
async def welcome():
    return {"massage": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

