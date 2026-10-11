from fastapi import FastAPI

from .api.routes import main_router
from src.core.config import Settings

app = FastAPI()


app.include_router(router=main_router)
