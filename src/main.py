from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.config import get_settings
from src.core.database import engine
from src.models import Base
from src.api.routes import main_router
from starlette.middleware.sessions import SessionMiddleware

from src.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
settings = get_settings()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.jwt.secret_key.get_secret_value()
)

app.include_router(main_router)