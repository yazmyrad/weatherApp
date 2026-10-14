from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.database import engine
from src.models import Base
from src.api.routes import main_router

from src.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(main_router)