from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.core.security import verify_password, hash_password
from app.models import User, Blog, BlogImage
import math


# -------------------------------user-------------------------------
def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).one_or_none()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user

def create_user(db: Session, user_data):
    existing_user = db.query(User).filter(User.email == user_data.email).one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hash_pw = hash_password(user_data.password)

    new_user = User(name = user_data.name,email=user_data.email, password=hash_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user) # take new data from db

    return new_user


def update_user(user: User, update_data, db: Session):
    f_update_data = update_data.dict(exclude_unset=True) # delete the key have none value
    print(f_update_data)

    if f_update_data.get('email') and user.email != f_update_data['email']:

        existing_email = db.query(User).filter(User.email == f_update_data['email']).one_or_none()

        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")

    if f_update_data.get('password'):
        hash_pw = hash_password(f_update_data['password'])
        f_update_data['password'] = hash_pw

    for key, value in f_update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).one_or_none()


# -------------------------------blog-------------------------------
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

def blog_detail_service(db: Session, blog_id: int):
    blog = db.query(Blog).filter(Blog.id == blog_id).one_or_none()

    return blog

def update_blog_service(db: Session, blog_data):
    pass