# Домашнее задание по теме "Модели данных Pydantic"
# Задача "Модель пользователя"

from fastapi import FastAPI, Body, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
def get_main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/users")
def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int) -> User:
    user_id = (users[-1].id + 1 if len(users) > 0 else 1)
    users.append(User(id=user_id, username=username, age=age))
    return users[-1]


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int) -> User:
    try:
        gen = (users[i] for i in range(len(users)) if users[i].id == user_id)
        edit_user = next(gen)
    except StopIteration or IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
    else:
        edit_user.username = username
        edit_user.age = age
        return edit_user


@app.delete("/user/{user_id}")
def delete_user(user_id: int) -> User:
    try:
        gen = (users[i] for i in range(len(users)) if len(users) > 0 and users[i].id == user_id)
        j = (i for i in range(len(users)) if len(users) > 0 and users[i].id == user_id)
        edit_user = next(gen)
        indx = next(j)
    except StopIteration or IndexError or NameError:
        raise HTTPException(status_code=404, detail="User was not found")
    else:
        users.pop(indx)
        return edit_user


@app.delete("/")
async def delete_all_users() -> str:
    users.clear()
    return "All users were deleted"
