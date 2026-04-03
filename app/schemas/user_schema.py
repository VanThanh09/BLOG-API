from typing import Optional

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    avatar: Optional[str] = None

    def get_avatar(self):
        return self.avatar if self.avatar else "https://res.cloudinary.com/drzc4fmxb/image/upload/v1733907010/xvethjfe9cycrroqi7po.jpg"


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    avatar: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    avatar: str

    class Config:
        from_attributes = True


