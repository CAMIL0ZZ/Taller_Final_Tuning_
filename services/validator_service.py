from fastapi import HTTPException
from app.database.supabase_client import supabase


class ValidatorService:

    @staticmethod
    def user_exists(user_id: int):
        result = (
            supabase.table("users")
            .select("id")
            .eq("id", user_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                status_code=404,
                detail=f"User {user_id} not found"
            )

    @staticmethod
    def stock_car_exists(stock_car_id: int):
        result = (
            supabase.table("stock_cars")
            .select("id")
            .eq("id", stock_car_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                status_code=404,
                detail=f"Stock car {stock_car_id} not found"
            )

    @staticmethod
    def build_exists(build_id: int):
        result = (
            supabase.table("builds")
            .select("id")
            .eq("id", build_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                status_code=404,
                detail=f"Build {build_id} not found"
            )

    @staticmethod
    def mod_exists(mod_id: int):
        result = (
            supabase.table("mods")
            .select("id")
            .eq("id", mod_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                status_code=404,
                detail=f"Mod {mod_id} not found"
            )