from fastapi import FastAPI

from app.routers import user_router, blog_router
from app.db.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(blog_router.router)