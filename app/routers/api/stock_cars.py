from fastapi import APIRouter, UploadFile, File

from app.services.stock_car_service import (
    StockCarService
)

from app.models.stock_car import (
    StockCarCreate,
    StockCarUpdate
)

router = APIRouter(
    prefix="/stock-cars",
    tags=["Stock Cars"]
)


@router.get("/")
def get_stock_cars(
    fuel: str = None,
    chassis_type: str = None
):
    return StockCarService.get_all(
        fuel,
        chassis_type
    )


@router.get("/{car_id}")
def get_stock_car(car_id: int):
    return StockCarService.get_by_id(car_id)


@router.post("/")
def create_stock_car(
    stock_car: StockCarCreate
):
    return StockCarService.create(
        stock_car.model_dump()
    )


@router.put("/{car_id}")
def update_stock_car(
    car_id: int,
    stock_car: StockCarUpdate
):
    return StockCarService.update(
        car_id,
        stock_car.model_dump(
            exclude_unset=True
        )
    )


@router.delete("/{car_id}")
def delete_stock_car(car_id: int):
    return StockCarService.delete(car_id)

@router.post("/{car_id}/picture")
def upload_picture(
    car_id: int,
    file: UploadFile = File(...)
):
    return StockCarService.upload_picture(
        car_id,
        file
    )