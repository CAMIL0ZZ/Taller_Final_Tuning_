from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr
    description: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    description: Optional[str] = None
 #   picture: Optional[str] = None


class UserResponse(UserBase):
    id: int
    picture: Optional[str] = None

    model_config = {
        "from_attributes": True
    }


"""
from pydantic import (
    BaseModel,
    EmailStr,
    Field
)
from typing import Optional


class UserBase(BaseModel):

    username: str = Field(
        min_length=3,
        max_length=30
    )

    email: EmailStr

    description: Optional[str] = Field(
        default=None,
        max_length=300
    )


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):

    username: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=30
    )

    email: Optional[EmailStr] = None

    description: Optional[str] = Field(
        default=None,
        max_length=300
    )


class UserResponse(UserBase):

    id: int
    picture: Optional[str] = None

    model_config = {
        "from_attributes": True
    }

"""