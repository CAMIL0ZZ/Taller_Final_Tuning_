from pydantic import (
    BaseModel,
    Field
)
from typing import Optional

from app.enums.build_approach import BuildApproach


class BuildBase(BaseModel):

    user_id: int = Field(
        gt=0
    )

    stock_car_id: int = Field(
        gt=0
    )

    build_name: str = Field(
        min_length=3,
        max_length=60
    )

    build_approach: BuildApproach

    engine: str = Field(
        min_length=2,
        max_length=80
    )

    year: int = Field(
        ge=1900,
        le=2100
    )

    hp: int = Field(
        gt=0,
        le=5000
    )

    price: float = Field(
        gt=0
    )


class BuildCreate(BuildBase):
    pass


class BuildUpdate(BaseModel):

    user_id: Optional[int] = Field(
        default=None,
        gt=0
    )

    stock_car_id: Optional[int] = Field(
        default=None,
        gt=0
    )

    build_name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=60
    )

    build_approach: Optional[
        BuildApproach
    ] = None

    engine: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=80
    )

    year: Optional[int] = Field(
        default=None,
        ge=1900,
        le=2100
    )

    hp: Optional[int] = Field(
        default=None,
        gt=0,
        le=5000
    )

    price: Optional[float] = Field(
        default=None,
        gt=0
    )


class BuildResponse(BuildBase):

    id: int
    picture: Optional[str] = None

    model_config = {
        "from_attributes": True
    }