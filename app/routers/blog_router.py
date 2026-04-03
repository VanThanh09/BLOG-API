from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db, get_current_user
from app.schemas.blog_schema import Blog, BlogPost
from app.services.blog_service import create_blog_service, blog_list_service

router = APIRouter(prefix="/blogs", tags=["blogs"])

@router.post("/create", response_model=Blog)
def create_blog_router(blog_data: BlogPost, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        new_blog = create_blog_service(db=db, blog_data=blog_data, author=current_user)
        return new_blog
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/list")
def list_blog_router(page: int, db: Session = Depends(get_db)):
    try:
        list_blog = blog_list_service(db, page=page)
        return list_blog
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))