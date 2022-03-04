from fastapi import APIRouter

from .users import router as user_route
from .router import router as main_route

api_route = APIRouter()
api_route.include_router(user_route)
api_route.include_router(main_route)

