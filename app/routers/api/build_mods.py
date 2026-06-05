from fastapi import APIRouter

from app.services.build_mod_service import (
    BuildModService
)

from app.models.build_mod import (
    BuildModCreate,
    BuildModUpdate
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

@router.put("/{relation_id}")
def update_relation(
    relation_id: int,
    relation: BuildModUpdate
):
    return BuildModService.update(
        relation_id,
        relation.model_dump(
            exclude_unset=True
        )
    )

@router.get("/mod/{mod_id}")
def get_mod_builds(
    mod_id: int
):
    return BuildModService.get_by_mod(
        mod_id
    )

@router.get("/build/{build_id}")
def get_build_mods(
    build_id: int
):
    return BuildModService.get_mods_by_build(
        build_id
    )