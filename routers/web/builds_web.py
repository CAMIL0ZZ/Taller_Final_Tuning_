from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.services.build_service import (
    BuildService
)

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

    return templates.TemplateResponse(
        "builds/detail.html",
        {
            "request": request,
            "build": build
        }
    )