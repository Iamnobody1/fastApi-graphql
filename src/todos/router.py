from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, service
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_user = service.get_todo_by_title(db, title=todo.title)
    if db_user:
        raise HTTPException(status_code=400, detail="Title already registered")
    return service.create_todo(db=db, todo=todo)


@router.get("/", response_model=list[schemas.Todo])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = service.get_todos(db, skip=skip, limit=limit)
    return users


@router.get("/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_user = service.get_todo(db, id=todo_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{todo_id}")
def update_todo(todo_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = service.update_todo(db, id=todo_id, todo=todo)
    return todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = service.delete_todo(db, id=todo_id)
    return todo
