from fastapi import FastAPI
import uvicorn
from .api.routes import main_router

app = FastAPI()
app.include_router(main_router)
