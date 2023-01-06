from pydantic import typing
import strawberry
from strawberry.types import Info
from ..scalars.todo_scalar import Todo

from ..resolvers.todo_resolver import get_todo, get_todos


@strawberry.type
class Query:
    @strawberry.field
    async def todos(self, info: Info) -> typing.List[Todo]:
        """Get all todos"""
        todos_data_list = await get_todos(info)
        return todos_data_list

    @strawberry.field
    async def todo(self, info: Info, todo_id: int) -> Todo:
        """Get todo by id"""
        todo_dict = await get_todo(todo_id, info)
        return todo_dict
