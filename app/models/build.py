from pydantic import BaseModel
from typing import Optional


class BuildModCreate(BaseModel):
    build_id: int
    mod_id: int


class BuildModResponse(BaseModel):
    id: int
    build_id: int
    mod_id: int

    model_config = {
        "from_attributes": True
    }

class BuildModUpdate(BaseModel):

    build_id: Optional[int] = None
    mod_id: Optional[int] = None


"""
from pydantic import (
    BaseModel,
    Field
)
from typing import Optional


class BuildModCreate(BaseModel):

    build_id: int = Field(
        gt=0
    )

    mod_id: int = Field(
        gt=0
    )


class BuildModUpdate(BaseModel):

    build_id: Optional[int] = Field(
        default=None,
        gt=0
    )

    mod_id: Optional[int] = Field(
        default=None,
        gt=0
    )


class BuildModResponse(BaseModel):

    id: int
    build_id: int
    mod_id: int

    model_config = {
        "from_attributes": True
    }

"""