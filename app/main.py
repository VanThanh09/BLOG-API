from fastapi import FastAPI

from app.api.main import api_router
from app.core.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(api_router)