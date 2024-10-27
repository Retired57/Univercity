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
def create_user(username: str, age: int, new_user: User) -> User:
    new_user.id = (users[len(users) - 1].id + 1 if len(users) > 0 else 1)
    new_user.username = username
    new_user.age = age
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int) -> User:
    try:
        gen = (users[i] for i in range(len(users)) if len(users) > 0 and users[i].id == user_id)
        edit_user = list(gen)[0]
    except IndexError:
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
        edit_user = list(gen)[0]
        indx = list(j)[0]
        return edit_user
    except:
        raise HTTPException(status_code=404, detail="User was not found")
    finally:
        try:
            indx
        except NameError:
            raise HTTPException(status_code=404, detail="User was not found")
        else:
            users.pop(indx)


@app.delete("/")
async def delete_all_users() -> str:
    users.clear()
    return "All users were deleted"
