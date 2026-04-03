from fastapi import APIRouter

from app.api.routes import blog_router, user_router

api_router = APIRouter()

api_router.include_router(user_router.router)
api_router.include_router(blog_router.router)