from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://admin:pwd1234@localhost:5432/todox"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

async_session = sessionmaker(
    autocommit=False,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    bind=engine,
)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()


Base = declarative_base()
