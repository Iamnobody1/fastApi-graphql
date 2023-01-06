from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import load_only
from ...database import get_session
from ..helpers.helper import get_valid_data
from ..models import todo_model
from ..scalars.todo_scalar import AddTodo, Todo, TodoDeleted, TodoExists, TodoNotFound


async def get_todos():
    async with get_session() as s:
        sql = select(todo_model.Todo).order_by(todo_model.Todo.title)
        db_todos = (await s.execute(sql)).scalars().unique().all()

    todos_data_list = []
    for todo in db_todos:
        todo_dict = get_valid_data(todo, todo_model.Todo)
        todos_data_list.append(Todo(**todo_dict))

    return todos_data_list


async def get_todo(todo_id):
    async with get_session() as s:
        sql = (
            select(todo_model.Todo)
            .filter(todo_model.Todo.id == todo_id)
            .order_by(todo_model.Todo.title)
        )
        db_todo = (await s.execute(sql)).scalars().unique().one()

    todo_dict = get_valid_data(db_todo, todo_model.Todo)
    return Todo(**todo_dict)


async def add_todo(title):
    async with get_session() as s:
        sql = (
            select(todo_model.Todo)
            .options(load_only("title"))
            .filter(todo_model.Todo.title == title)
        )
        existing_db_todo = (await s.execute(sql)).first()
        if existing_db_todo is not None:
            return TodoExists()

        query = insert(todo_model.Todo).values(title=title)
        await s.execute(query)

        sql = select(todo_model.Todo).filter(todo_model.Todo.title == title)
        db_todo = (await s.execute(sql)).scalars().unique().one()
        await s.commit()

    db_todo_serialize_data = db_todo.as_dict()
    return AddTodo(**db_todo_serialize_data)


async def update_todo(todo_id, title, completed):
    async with get_session() as s:
        sql = select(todo_model.Todo).where(todo_model.Todo.id == todo_id)
        existing_db_todo = (await s.execute(sql)).first()
        if existing_db_todo is None:
            return TodoNotFound()

        query = (
            update(todo_model.Todo)
            .where(todo_model.Todo.id == todo_id)
            .values(title=title, completed=completed)
        )
        await s.execute(query)

        sql = select(todo_model.Todo).where(todo_model.Todo.id == todo_id)
        db_todo = (await s.execute(sql)).scalars().unique().one()
        await s.commit()

    db_todo_serialize_data = db_todo.as_dict()
    return Todo(**db_todo_serialize_data)


async def delete_todo(todo_id):
    async with get_session() as s:
        sql = select(todo_model.Todo).where(todo_model.Todo.id == todo_id)
        existing_db_todo = (await s.execute(sql)).first()
        if existing_db_todo is None:
            return TodoNotFound()

        query = delete(todo_model.Todo).where(todo_model.Todo.id == todo_id)
        await s.execute(query)
        await s.commit()

    return TodoDeleted()
