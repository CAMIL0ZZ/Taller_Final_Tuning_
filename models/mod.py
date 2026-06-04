from pydantic import BaseModel
from typing import Optional

from app.enums.mod_type import ModType


class ModBase(BaseModel):
    name: str
    description: str
    type_mod: ModType
    price: float


class ModCreate(ModBase):
    pass


class ModUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    type_mod: Optional[ModType] = None
    price: Optional[float] = None


class ModResponse(ModBase):
    id: int

    model_config = {
        "from_attributes": True
    }