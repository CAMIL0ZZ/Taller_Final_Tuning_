from fastapi import HTTPException

from app.database.supabase_client import supabase
from app.services.upload_service import UploadService


class StockCarService:

    @staticmethod
    def get_all(
        fuel=None,
        chassis_type=None
    ):

        query = (
            supabase.table("stock_cars")
            .select("*")
        )

        if fuel:
            query = query.eq("fuel", fuel)

        if chassis_type:
            query = query.eq(
                "chassis_type",
                chassis_type
            )

        return query.execute().data

    @staticmethod
    def get_by_id(car_id: int):

        result = (
            supabase.table("stock_cars")
            .select("*")
            .eq("id", car_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                404,
                "Stock car not found"
            )

        return result.data[0]

    @staticmethod
    def create(data: dict):

        return (
            supabase.table("stock_cars")
            .insert(data)
            .execute()
            .data[0]
        )

    @staticmethod
    def update(car_id: int, data: dict):

        StockCarService.get_by_id(car_id)

        return (
            supabase.table("stock_cars")
            .update(data)
            .eq("id", car_id)
            .execute()
            .data[0]
        )

    @staticmethod
    def delete(car_id: int):

        StockCarService.get_by_id(car_id)

        builds = (
            supabase.table("builds")
            .select("id")
            .eq("stock_car_id", car_id)
            .execute()
        )

        if builds.data:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Cannot delete stock car because it is "
                    "used by one or more builds."
                )
            )

        supabase.table("stock_cars") \
            .delete() \
            .eq("id", car_id) \
            .execute()

        return {
            "message": "Stock car deleted"
        }

    @staticmethod
    def upload_picture(car_id, file):

        StockCarService.get_by_id(car_id)

        image_url = UploadService.upload_entity_picture(
            "stock_cars",
            car_id,
            file
        )

        supabase.table("stock_cars") \
            .update({"picture": image_url}) \
            .eq("id", car_id) \
            .execute()

        return {
            "picture": image_url
        }