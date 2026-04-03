from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class Author(BaseModel):
    name: str
    avatar: str


class Image(BaseModel):
    url: str


class BlogList(BaseModel):
    title: Optional[str] = None
    content: str
    created_at: datetime
    author: Author
    images: Optional[List[Image]] = None

    class Config:
        from_attributes = True


class BlogPost(BaseModel):
    title: Optional[str] = None
    content: str
    is_published: bool

    images: Optional[List[Image]] = None


class Blog(BaseModel):
    id: int
    title: Optional[str] = None
    content: str
    is_published: bool
    created_at: datetime
    author: Author
    images: Optional[List[Image]] = None
