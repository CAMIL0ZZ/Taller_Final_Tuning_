from fastapi import HTTPException

from app.database.supabase_client import supabase
from app.services.validator_service import ValidatorService


class BuildModService:

    @staticmethod
    def get_all():

        return (
            supabase.table("build_mods")
            .select("*")
            .execute()
            .data
        )

    @staticmethod
    def create(data: dict):

        ValidatorService.build_exists(
            data["build_id"]
        )

        ValidatorService.mod_exists(
            data["mod_id"]
        )

        duplicated = (
            supabase.table("build_mods")
            .select("*")
            .eq(
                "build_id",
                data["build_id"]
            )
            .eq(
                "mod_id",
                data["mod_id"]
            )
            .execute()
        )

        if duplicated.data:
            raise HTTPException(
                409,
                "Mod already assigned"
            )

        result = (
            supabase.table("build_mods")
            .insert(data)
            .execute()
        )

        return result.data[0]

    @staticmethod
    def delete(relation_id: int):

        result = (
            supabase.table("build_mods")
            .select("*")
            .eq("id", relation_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                404,
                "Relation not found"
            )

        supabase.table("build_mods") \
            .delete() \
            .eq("id", relation_id) \
            .execute()

        return {
            "message": "Relation deleted"
        }

    @staticmethod
    def update(
            relation_id: int,
            data: dict
    ):

        relation = (
            supabase.table("build_mods")
            .select("*")
            .eq("id", relation_id)
            .execute()
        )

        if not relation.data:
            raise HTTPException(
                404,
                "Relation not found"
            )

        if "build_id" in data:
            ValidatorService.build_exists(
                data["build_id"]
            )

        if "mod_id" in data:
            ValidatorService.mod_exists(
                data["mod_id"]
            )

        new_build = data.get(
            "build_id",
            relation.data[0]["build_id"]
        )

        new_mod = data.get(
            "mod_id",
            relation.data[0]["mod_id"]
        )

        duplicated = (
            supabase.table("build_mods")
            .select("*")
            .eq("build_id", new_build)
            .eq("mod_id", new_mod)
            .neq("id", relation_id)
            .execute()
        )

        if duplicated.data:
            raise HTTPException(
                409,
                "Relation already exists"
            )

        return (
            supabase.table("build_mods")
            .update(data)
            .eq("id", relation_id)
            .execute()
            .data[0]
        )

    @staticmethod
    def get_by_mod(
            mod_id: int
    ):

        ValidatorService.mod_exists(
            mod_id
        )

        return (
            supabase.table("build_mods")
            .select(
                "*, builds(*)"
            )
            .eq("mod_id", mod_id)
            .execute()
            .data
        )

    @staticmethod
    def get_mods_by_build(
            build_id: int
    ):

        ValidatorService.build_exists(
            build_id
        )

        return (
            supabase.table("build_mods")
            .select(
                "*, mods(*)"
            )
            .eq(
                "build_id",
                build_id
            )
            .execute()
            .data
        )