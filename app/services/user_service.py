from fastapi import HTTPException
from typing import Optional

from app.models.user import User
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate

def create_user(db: Session, user: UserCreate) -> Optional[User]:
    try:
        user = User(**user.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()

        error_msg = str(e.orig)

        if "users.username" in error_msg:
            raise HTTPException(409, "Username already exists")

        if "users.email" in error_msg:
            raise HTTPException(409, "Email already exists")

        raise HTTPException(status_code=500, detail="can not create user-service: " + str(e))

def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).one_or_none()