import strawberry
from pydantic import typing


@strawberry.type
class Todo:
    id: int
    title: typing.Optional[str] = ""


@strawberry.type
class AddTodo:
    id: int
    title: typing.Optional[str] = ""


@strawberry.type
class TodoExists:
    message: str = "Todo with this title already exists"


@strawberry.type
class TodoNotFound:
    message: str = "Couldn't find todo with the supplied id"


@strawberry.type
class TodoTitleMissing:
    message: str = "Please supply todo title"


@strawberry.type
class TodoIdMissing:
    message: str = "Please supply todo id"


@strawberry.type
class TodoDeleted:
    message: str = "Todo deleted"
