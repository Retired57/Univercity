# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Задача "Имитация работы с БД"


from fastapi import FastAPI, Path

app = FastAPI()

users_db = {"1": "Имя: Example, возраст: 18"}


@app.get("/")
async def get_main_page() -> str:
    return "Main page"


@app.get("/users")
async def get_all_users() -> dict:
    return users_db


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    user_id = str(int(max(users_db, key=int)) + 1)
    users_db[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int) -> str:
    users_db[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users_db.pop(user_id)
    return f"User with id {user_id} is deleted"


@app.delete("/")
async def delete_all_users() -> str:
    users_db.clear()
    return "All users are deleted"
