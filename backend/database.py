import asyncio
from sqlalchemy import URL, text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncAttrs, async_sessionmaker
from sqlalchemy.orm import Session, Mapped, mapped_column, declarative_base
from backend.config import settings
from sqlalchemy import Integer

engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)

# Create a new sessionmaker
async_sess_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_db_session():
    async with async_sess_maker() as session:
        yield session

Base = declarative_base()