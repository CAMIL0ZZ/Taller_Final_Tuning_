from pydantic import (
    BaseModel,
    Field
)
from typing import Optional

from app.enums.mod_type import ModType


class ModBase(BaseModel):

    type_mod: ModType

    brand: str = Field(
        min_length=2,
        max_length=40
    )

    reference: str = Field(
        min_length=1,
        max_length=50
    )

    name: str = Field(
        min_length=2,
        max_length=80
    )

    price: float = Field(
        gt=0
    )


class ModCreate(ModBase):
    pass


class ModUpdate(BaseModel):

    type_mod: Optional[ModType] = None

    brand: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=40
    )

    reference: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50
    )

    name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=80
    )

    price: Optional[float] = Field(
        default=None,
        gt=0
    )


class ModResponse(ModBase):

    id: int
    picture: Optional[str] = None

    model_config = {
        "from_attributes": True
    }