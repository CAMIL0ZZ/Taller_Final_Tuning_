from fastapi import APIRouter, UploadFile, File

from app.services.mod_service import (
    ModService
)

from app.models.mod import (
    ModCreate,
    ModUpdate
)

router = APIRouter(
    prefix="/mods",
    tags=["Mods"]
)


@router.get("/")
def get_mods(
    type_mod: str = None
):
    return ModService.get_all(
        type_mod
    )


@router.get("/{mod_id}")
def get_mod(mod_id: int):
    return ModService.get_by_id(
        mod_id
    )


@router.post("/")
def create_mod(
    mod: ModCreate
):
    return ModService.create(
        mod.model_dump()
    )


@router.put("/{mod_id}")
def update_mod(
    mod_id: int,
    mod: ModUpdate
):
    return ModService.update(
        mod_id,
        mod.model_dump(
            exclude_unset=True
        )
    )


@router.delete("/{mod_id}")
def delete_mod(mod_id: int):
    return ModService.delete(
        mod_id
    )

@router.post("/{mod_id}/picture")
def upload_picture(
    mod_id: int,
    file: UploadFile = File(...)
):
    return ModService.upload_picture(
        mod_id,
        file
    )