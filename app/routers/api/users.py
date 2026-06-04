from fastapi import APIRouter, UploadFile, File

from app.services.user_service import UserService
from app.models.user import (
    UserCreate,
    UserUpdate
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/")
def get_users(
    username: str = None,
    email: str = None
):
    return UserService.get_all(
        username,
        email
    )


@router.get("/{user_id}")
def get_user(user_id: int):
    return UserService.get_by_id(user_id)


@router.post("/")
def create_user(user: UserCreate):
    return UserService.create(
        user.model_dump()
    )


@router.put("/{user_id}")
def update_user(
    user_id: int,
    user: UserUpdate
):
    return UserService.update(
        user_id,
        user.model_dump(exclude_unset=True)
    )


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return UserService.delete(user_id)


@router.post("/{user_id}/picture")
def upload_picture(
    user_id: int,
    file: UploadFile = File(...)
):
    return UserService.upload_picture(
        user_id,
        file
    )