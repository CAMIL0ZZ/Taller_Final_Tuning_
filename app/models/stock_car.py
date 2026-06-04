from pydantic import BaseModel
from typing import Optional

from app.enums.fuel_type import FuelType
from app.enums.chassis_type import ChassisType


class StockCarBase(BaseModel):
    brand: str
    model: str

    production_start: int
    production_end: int | None = None

    chassis_type: ChassisType
    fuel: FuelType

    price: float
    stock_hp: int


class StockCarCreate(StockCarBase):
    pass


class StockCarUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None

    production_start: Optional[int] = None
    production_end: Optional[int] = None

    chassis_type: Optional[ChassisType] = None
    fuel: Optional[FuelType] = None

    price: Optional[float] = None
    stock_hp: Optional[int] = None


class StockCarResponse(StockCarBase):
    id: int

    model_config = {
        "from_attributes": True
    }