from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.user_schema import UserResponse, UserCreate
from app.services import user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/create", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/profile", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_profile(username: str, db: Session = Depends(get_db)) -> Optional[UserResponse]:
    return user_service.get_user_by_username(db, username=username)