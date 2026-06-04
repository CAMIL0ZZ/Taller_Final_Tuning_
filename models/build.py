from pydantic import BaseModel
from typing import Optional

from app.enums.build_approach import BuildApproach


class BuildBase(BaseModel):
    name: str
    build_approach: BuildApproach
    price: float
    user_id: int
    stock_car_id: int


class BuildCreate(BuildBase):
    pass


class BuildUpdate(BaseModel):
    name: Optional[str] = None
    build_approach: Optional[BuildApproach] = None
    price: Optional[float] = None
    user_id: Optional[int] = None
    stock_car_id: Optional[int] = None


class BuildResponse(BuildBase):
    id: int

    model_config = {
        "from_attributes": True
    }