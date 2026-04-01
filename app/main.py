from fastapi import FastAPI

from app.core.security import hasd_password
from app.routers import user_router
from app.db.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

print(hasd_password("123456"))

app.include_router(user_router.router)