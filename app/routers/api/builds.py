from fastapi import APIRouter, UploadFile, File

from app.services.build_service import (
    BuildService
)

from app.models.build import (
    BuildCreate,
    BuildUpdate
)

router = APIRouter(
    prefix="/builds",
    tags=["Builds"]
)


@router.get("/")
def get_builds(
    build_approach: str = None
):
    return BuildService.get_all(
        build_approach
    )


@router.post("/")
def create_build(
    build: BuildCreate
):
    return BuildService.create(
        build.model_dump()
    )


@router.put("/{build_id}")
def update_build(
    build_id: int,
    build: BuildUpdate
):
    return BuildService.update(
        build_id,
        build.model_dump(
            exclude_unset=True
        )
    )


@router.delete("/{build_id}")
def delete_build(build_id: int):
    return BuildService.delete(
        build_id
    )


@router.get("/user/{user_id}")
def get_user_builds(
    user_id: int
):
    return BuildService.get_by_user(
        user_id
    )


@router.get("/car/{stock_car_id}")
def get_car_builds(
    stock_car_id: int
):
    return BuildService.get_by_car(
        stock_car_id
    )

@router.get("/{build_id}")
def get_build(build_id: int):
    return BuildService.get_by_id(
        build_id
    )

@router.post("/{build_id}/picture")
def upload_picture(
    build_id: int,
    file: UploadFile = File(...)
):
    return BuildService.upload_picture(
        build_id,
        file
    )