from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.services.stock_car_service import (
    StockCarService
)

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/stock-cars")
def stock_cars_page(
    request: Request
):

    cars = StockCarService.get_all()

    return templates.TemplateResponse(
        "stock_cars/list.html",
        {
            "request": request,
            "cars": cars
        }
    )


@router.get("/stock-cars/{car_id}")
def stock_car_detail(
    request: Request,
    car_id: int
):

    car = StockCarService.get_by_id(
        car_id
    )

    return templates.TemplateResponse(
        "stock_cars/detail.html",
        {
            "request": request,
            "car": car
        }
    )