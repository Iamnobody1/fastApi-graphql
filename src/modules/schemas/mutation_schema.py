import strawberry

from ..resolvers.todo_resolver import add_todo, delete_todo, update_todo
from ..fragments.todo_fragments import (
    AddTodoResponse,
    DeleteTodoResponse,
    UpdateTodoResponse,
)


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_todo(self, title: str) -> AddTodoResponse:
        add_todo_resp = await add_todo(title)
        return add_todo_resp

    @strawberry.mutation
    async def update_todo(
        self, todo_id: int, title: str, completed: bool
    ) -> UpdateTodoResponse:
        delete_todo_resp = await update_todo(todo_id, title, completed)
        return delete_todo_resp

    @strawberry.mutation
    async def delete_todo(self, todo_id: int) -> DeleteTodoResponse:
        delete_todo_resp = await delete_todo(todo_id)
        return delete_todo_resp
