from pydantic import (
    BaseModel,
    Field
)
from typing import Optional

from app.enums.fuel_type import FuelType
from app.enums.chassis_type import ChassisType


class StockCarBase(BaseModel):

    brand: str = Field(
        min_length=2,
        max_length=30
    )

    model: str = Field(
        min_length=1,
        max_length=50
    )

    production_start: int = Field(
        ge=1900,
        le=2027
    )

    production_end: Optional[int] = Field(
        default=None,
        ge=1900,
        le=2027
    )

    chassis_type: ChassisType
    fuel: FuelType

    price: float = Field(
        gt=0
    )

    stock_hp: int = Field(
        gt=0,
        le=5000
    )


class StockCarCreate(StockCarBase):
    pass


class StockCarUpdate(BaseModel):

    brand: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=30
    )

    model: Optional[str] = Field(
        default=None,
        min_length=1,
        max_length=50
    )

    production_start: Optional[int] = Field(
        default=None,
        ge=1900,
        le=2100
    )

    production_end: Optional[int] = Field(
        default=None,
        ge=1900,
        le=2100
    )

    chassis_type: Optional[ChassisType] = None
    fuel: Optional[FuelType] = None

    price: Optional[float] = Field(
        default=None,
        gt=0
    )

    stock_hp: Optional[int] = Field(
        default=None,
        gt=0,
        le=5000
    )


class StockCarResponse(StockCarBase):

    id: int
    picture: Optional[str] = None

    model_config = {
        "from_attributes": True
    }