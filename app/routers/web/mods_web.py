from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.services.mod_service import (
    ModService
)

from app.services.build_mod_service import (
    BuildModService
)

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/mods")
def mods_page(
    request: Request
):

    mods = ModService.get_all()

    return templates.TemplateResponse(
        "mods/list.html",
        {
            "request": request,
            "mods": mods
        }
    )


@router.get("/mods/{mod_id}")
def mod_detail(
    request: Request,
    mod_id: int
):

    mod = ModService.get_by_id(
        mod_id
    )

    builds = (
        BuildModService.get_by_mod(
            mod_id
        )
    )

    return templates.TemplateResponse(
        "mods/detail.html",
        {
            "request": request,
            "mod": mod,
            "builds": builds
        }
    )