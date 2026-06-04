from fastapi import HTTPException

from app.database.supabase_client import supabase
from app.services.validator_service import ValidatorService


class BuildService:

    @staticmethod
    def get_all(build_approach=None):

        query = (
            supabase.table("builds")
            .select("*")
        )

        if build_approach:
            query = query.eq(
                "build_approach",
                build_approach
            )

        return query.execute().data

    @staticmethod
    def get_by_id(build_id: int):

        result = (
            supabase.table("builds")
            .select("*")
            .eq("id", build_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                404,
                "Build not found"
            )

        return result.data[0]

    @staticmethod
    def create(data: dict):

        ValidatorService.user_exists(
            data["user_id"]
        )

        ValidatorService.stock_car_exists(
            data["stock_car_id"]
        )

        return (
            supabase.table("builds")
            .insert(data)
            .execute()
            .data[0]
        )

    @staticmethod
    def update(build_id, data):

        BuildService.get_by_id(build_id)

        if "user_id" in data:
            ValidatorService.user_exists(
                data["user_id"]
            )

        if "stock_car_id" in data:
            ValidatorService.stock_car_exists(
                data["stock_car_id"]
            )

        return (
            supabase.table("builds")
            .update(data)
            .eq("id", build_id)
            .execute()
            .data[0]
        )

    @staticmethod
    def delete(build_id):

        BuildService.get_by_id(build_id)

        supabase.table("builds") \
            .delete() \
            .eq("id", build_id) \
            .execute()

        return {"message": "Build deleted"}

    @staticmethod
    def get_by_user(user_id: int):

        ValidatorService.user_exists(
            user_id
        )

        return (
            supabase.table("builds")
            .select("*")
            .eq("user_id", user_id)
            .execute()
            .data
        )

    @staticmethod
    def get_by_car(stock_car_id: int):

        ValidatorService.stock_car_exists(
            stock_car_id
        )

        return (
            supabase.table("builds")
            .select("*")
            .eq(
                "stock_car_id",
                stock_car_id
            )
            .execute()
            .data
        )