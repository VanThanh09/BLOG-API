import math
from sqlalchemy.orm import Session

from app.models import User, Blog, BlogImage

BLOG_PAGE_SIZE = 2


def create_blog_service(db: Session, blog_data, author: User):
    try:
        new_blog = Blog(title=blog_data.title, content=blog_data.content, author=author)
        if blog_data.is_published is not None:
            new_blog.is_published = blog_data.is_published

        db.add(new_blog)

        images = blog_data.images

        if images:
            for image in images:
                new_image = BlogImage(url=image.url, blog=new_blog)
                db.add(new_image)

        db.commit()
        db.refresh(new_blog)

        return new_blog
    except Exception as e:
        db.rollback()
        raise e


def blog_list_service(db: Session, page: int = 1):
    total_items = db.query(Blog).count()
    total_pages = math.ceil(total_items / BLOG_PAGE_SIZE)

    pagination = {
        "page": page,
        "page_size": BLOG_PAGE_SIZE,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1
    }

    blogs = db.query(Blog).limit(BLOG_PAGE_SIZE).offset((page - 1) * BLOG_PAGE_SIZE).all()

    return {
        "data": blogs,
        "pagination": pagination,
    }