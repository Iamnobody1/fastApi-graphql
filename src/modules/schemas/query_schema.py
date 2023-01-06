from pydantic import typing
import strawberry
from strawberry.types import Info
from ..scalars.todo_scalar import Todo

from ..resolvers.todo_resolver import get_todo, get_todos


@strawberry.type
class Query:
    @strawberry.field
    async def todos(self) -> typing.List[Todo]:
        todos_data_list = await get_todos()
        return todos_data_list

    @strawberry.field
    async def todo(self, todo_id: int) -> Todo:
        todo_dict = await get_todo(todo_id)
        return todo_dict
