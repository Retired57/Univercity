# Домашнее задание по теме "Структура проекта. Маршруты и модели Pydantic."
# Задача "Основные маршруты":

from fastapi import FastAPI
from routers import user
from routers import task

app = FastAPI()

@app.get("/")
async def welcome():
    return {"massage": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

