from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.api.perms import is_item_author
from app.schemas import Blog, BlogPost, BlogListResponse
from app.crud import create_blog_service, blog_list_service

router = APIRouter(prefix="/blogs", tags=["blogs"])

@router.post("/create", response_model=Blog)
def create_blog_router(blog_data: BlogPost, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    try:
        new_blog = create_blog_service(db=db, blog_data=blog_data, author=current_user)
        return new_blog
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("", response_model=BlogListResponse)
def list_blog_router(page: int, db: Session = Depends(get_db)):
    try:
        list_blog = blog_list_service(db, page=page)
        return list_blog
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.patch("/update/{blog_id}")
# def update_item(blog = Depends(is_item_author)): #check permission
#
#     return {"message": "Updated", "item": blog}

# async def upload_image(file: UploadFile = File(...)):
