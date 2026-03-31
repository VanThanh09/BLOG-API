from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    username: str
    password: str
    is_active: bool
    avatar: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    username: str
    is_active: bool
    avatar: str

    class Config:
        from_attributes = True