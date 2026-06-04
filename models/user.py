from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    picture: Optional[str] = None


class UserResponse(UserBase):
    id: int
    picture: Optional[str] = None

    model_config = {
        "from_attributes": True
    }