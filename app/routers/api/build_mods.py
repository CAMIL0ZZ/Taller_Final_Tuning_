from fastapi import APIRouter

from app.services.build_mod_service import (
    BuildModService
)

from app.models.build_mod import (
    BuildModCreate
)

router = APIRouter(
    prefix="/build-mods",
    tags=["Build Mods"]
)


@router.get("/")
def get_relations():
    return BuildModService.get_all()


@router.post("/")
def create_relation(
    relation: BuildModCreate
):
    return BuildModService.create(
        relation.model_dump()
    )


@router.delete("/{relation_id}")
def delete_relation(
    relation_id: int
):
    return BuildModService.delete(
        relation_id
    )