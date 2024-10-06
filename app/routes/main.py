from fastapi import APIRouter
from app.routes.user import router as user

api_router = APIRouter(prefix="/api", tags=["API"])

api_router.include_router(user.router, prefix="/login")
