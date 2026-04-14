from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException

from app import crud
from app.core.config import redis_client
from app.core.security import decode_token
from app.core.database import SessionLocal
from sqlalchemy.orm import Session
from app.models import User
import json

from app.schemas import UserResponse


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_redis():
    return redis_client

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login") # get token from header

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db), redis=Depends(get_redis)):
    payload = decode_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token - Login again")

    user_email = payload.get("sub")

    #check cache
    key = f"user:{user_email}"

    cached = redis.get(key)
    if cached:
        return UserResponse.model_validate_json(cached)

    #db query
    user = crud.get_user_by_email(db, user_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    #set cache
    user_schema = UserResponse.model_validate(user)
    redis.set(key, user_schema.model_dump_json(), ex=300)

    return user

