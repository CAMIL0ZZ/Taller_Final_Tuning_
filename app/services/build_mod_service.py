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