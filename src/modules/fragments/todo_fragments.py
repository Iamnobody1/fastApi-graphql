import strawberry

from ..scalars.todo_scalar import (
    Todo,
    AddTodo,
    TodoDeleted,
    TodoExists,
    TodoIdMissing,
    TodoNotFound,
)


AddTodoResponse = strawberry.union("AddTodoResponse", (AddTodo, TodoExists))
UpdateTodoResponse = strawberry.union("UpdateTodoResponse", (Todo, TodoNotFound))
DeleteTodoResponse = strawberry.union(
    "DeleteTodoResponse", (TodoDeleted, TodoNotFound, TodoIdMissing)
)
