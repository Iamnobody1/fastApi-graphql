import strawberry

from ..resolvers.todo_resolver import add_todo, delete_todo
from ..fragments.todo_fragments import AddTodoResponse, DeleteTodoResponse


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_todo(self, name: str) -> AddTodoResponse:
        add_todo_resp = await add_todo(name)
        return add_todo_resp

    @strawberry.mutation
    async def delete_todo(self, todo_id: int) -> DeleteTodoResponse:
        delete_todo_resp = await delete_todo(todo_id)
        return delete_todo_resp
