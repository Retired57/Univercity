# Домашнее задание по теме "Шаблонизатор Jinja 2."
# Задача "Список пользователей в шаблоне"

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# templates = Jinja2Templates(directory="Module_16/templates")


users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        gen = (users[i] for i in range(len(users)) if users[i].id == user_id)
        # get_user = next(gen)
        return templates.TemplateResponse("users.html", {"request": request, "user": next(gen)})
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.post("/user/{username}/{age}")
def post_user(request: Request, username: str, age: int) -> HTMLResponse:
    if users:
        user_id = max(users, key=lambda m: m.id).id + 1
    else:
        user_id = 1
    users.append(User(id=user_id, username=username, age=age))
    return templates.TemplateResponse("users.html", {"request": request, "user": users[-1]})


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
def delete_user(user_id: int) -> str:
    try:
        gen = (users[i] for i in range(len(users)) if len(users) > 0 and users[i].id == user_id)
        users.remove(next(gen))
        return f"User ID={user_id} is deleted"
    except StopIteration or IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
