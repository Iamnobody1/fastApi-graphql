from fastapi import FastAPI
from .todos import router as todos

app = FastAPI()

app.include_router(todos.router)
