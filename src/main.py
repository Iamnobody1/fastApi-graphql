from fastapi import FastAPI
from .todos import router as todos

app = FastAPI()

app.include_router(todos.router)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
