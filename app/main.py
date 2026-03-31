from fastapi import FastAPI
from app.routers import user_router
from app.db.database import Base, engine
from app.models import user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)