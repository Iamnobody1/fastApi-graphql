import strawberry

from ..scalars.todo_scalar import (
    AddTodo,
    TodoDeleted,
    TodoExists,
    TodoIdMissing,
    TodoNotFound,
)


AddTodoResponse = strawberry.union("AddTodoResponse", (AddTodo, TodoExists))
DeleteTodoResponse = strawberry.union(
    "DeleteTodoResponse", (TodoDeleted, TodoNotFound, TodoIdMissing)
)
