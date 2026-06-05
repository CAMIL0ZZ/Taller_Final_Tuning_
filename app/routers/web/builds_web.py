from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.services.build_service import (
    BuildService
)

from app.services.build_mod_service import (
    BuildModService
)

from app.services.user_service import UserService
from app.services.stock_car_service import StockCarService


router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/builds")
def builds_page(
    request: Request
):

    builds = BuildService.get_all()

    return templates.TemplateResponse(
        "builds/list.html",
        {
            "request": request,
            "builds": builds
        }
    )


@router.get("/builds/{build_id}")
def build_detail(
    request: Request,
    build_id: int
):

    build = BuildService.get_by_id(
        build_id
    )

    user = UserService.get_by_id(
        build["user_id"]
    )

    stock_car = (
        StockCarService.get_by_id(
            build["stock_car_id"]
        )
    )

    mods = (
        BuildModService.get_mods_by_build(
            build_id
        )
    )

    return templates.TemplateResponse(
        "builds/detail.html",
        {
            "request": request,
            "build": build,
            "user": user,
            "stock_car": stock_car,
            "mods": mods
        }
    )
