from fastapi import APIRouter, Depends, status, HTTPException

# Сессия БД
from sqlalchemy.orm import Session

# Функция подключения к БД
from ..backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from ..models import User, Task
from ..schemas import CreateUser, CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found")
    return task


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask, user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found")
    else:
        db.execute(insert(Task).values(title=create_task.title,
                                       content=create_task.content,
                                       priority=create_task.priority,
                                       user_id=user_id,
                                       slug=slugify(create_task.title)))
        db.commit()
        return {
            "status_code": status.HTTP_201_CREATED,
            "transaction": "Successful"
        }


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], task_id: int, task_update: UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
    db.execute(update(Task).where(Task.id == task_id).values(
        title=task_update.title,
        content=task_update.content,
        priority=task_update.priority))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Task has been successfully updated"
    }


@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task was not found"
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Task has been successfully deleted"
    }