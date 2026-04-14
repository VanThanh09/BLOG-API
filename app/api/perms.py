from fastapi import Depends, HTTPException
from app.api.deps import get_current_user, get_db
from app import crud, models

def is_item_author(blog_id: int, current_user = Depends(get_current_user), db = Depends(get_db)):
    blog = crud.blog_detail_service(db, blog_id)

    if not blog:
        raise HTTPException(status_code=404, detail="Item not found")

    if blog.author.id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return blog