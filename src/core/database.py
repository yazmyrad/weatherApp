from sqlalchemy.ext.asyncio import create_async_engine
from .config import get_settings
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from collections.abc import AsyncGenerator

settings = get_settings()

engine = create_async_engine(settings.database.url, echo=False)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session