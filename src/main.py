from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from .modules.schemas.mutation_schema import Mutation
from .modules.schemas.query_schema import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
