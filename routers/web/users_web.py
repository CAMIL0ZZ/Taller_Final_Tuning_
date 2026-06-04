
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from app.services.user_service import (
    UserService
)

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/users")
def users_page(
    request: Request
):

    users = UserService.get_all()

    return templates.TemplateResponse(
        "users/list.html",
        {
            "request": request,
            "users": users
        }
    )


@router.get("/users/{user_id}")
def user_detail(
    request: Request,
    user_id: int
):

    user = UserService.get_by_id(
        user_id
    )

    return templates.TemplateResponse(
        "users/detail.html",
        {
            "request": request,
            "user": user
        }
    )