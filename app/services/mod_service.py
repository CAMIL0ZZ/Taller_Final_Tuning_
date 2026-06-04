from fastapi import HTTPException

from app.database.supabase_client import supabase


class ModService:

    @staticmethod
    def get_all(type_mod=None):

        query = (
            supabase.table("mods")
            .select("*")
        )

        if type_mod:
            query = query.eq(
                "type_mod",
                type_mod
            )

        return query.execute().data

    @staticmethod
    def get_by_id(mod_id):

        result = (
            supabase.table("mods")
            .select("*")
            .eq("id", mod_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                404,
                "Mod not found"
            )

        return result.data[0]

    @staticmethod
    def create(data):

        return (
            supabase.table("mods")
            .insert(data)
            .execute()
            .data[0]
        )

    @staticmethod
    def update(mod_id, data):

        ModService.get_by_id(mod_id)

        return (
            supabase.table("mods")
            .update(data)
            .eq("id", mod_id)
            .execute()
            .data[0]
        )

    @staticmethod
    def delete(mod_id):

        ModService.get_by_id(mod_id)

        supabase.table("mods") \
            .delete() \
            .eq("id", mod_id) \
            .execute()

        return {"message": "Mod deleted"}