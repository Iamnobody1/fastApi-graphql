from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import models, schemas


def get_todo(db: Session, id: int):
    return db.query(models.Todo).filter(models.Todo.id == id).first()


def get_todo_by_title(db: Session, title: str):
    return db.query(models.Todo).filter(models.Todo.title == title).first()


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_user = models.Todo(title=todo.title, completed=todo.completed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_todo(db: Session, id: int, todo: schemas.TodoUpdate):
    item = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    todo_data = todo.dict(exclude_unset=True)
    for key, value in todo_data.items():
            setattr(item, key, value)
    print("1", item)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def delete_todo(db: Session, id: int):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(todo)
    db.commit()
    return {"ok": True}
