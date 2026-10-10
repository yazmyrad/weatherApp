from .users import router as userRouter
from .auth import router as authRouter
from .weather import router as weatherRouter
from .geo import router as geoRouter

from fastapi import APIRouter

main_router = APIRouter()

main_router.include_router(userRouter)
main_router.include_router(authRouter)
main_router.include_router(weatherRouter)
main_router.include_router(geoRouter)

