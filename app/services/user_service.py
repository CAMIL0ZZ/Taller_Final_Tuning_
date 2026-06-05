from fastapi import HTTPException

from app.database.supabase_client import supabase
from app.services.upload_service import UploadService


class UserService:

    @staticmethod
    def get_all(username=None, email=None):

        query = supabase.table("users").select("*")

        if username:
            query = query.ilike(
                "username",
                f"%{username}%"
            )

        if email:
            query = query.ilike(
                "email",
                f"%{email}%"
            )

        return query.execute().data

    @staticmethod
    def get_by_id(user_id: int):

        result = (
            supabase.table("users")
            .select("*")
            .eq("id", user_id)
            .execute()
        )

        if not result.data:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return result.data[0]

    @staticmethod
    def create(data: dict):

        result = (
            supabase.table("users")
            .insert(data)
            .execute()
        )

        return result.data[0]

    @staticmethod
    def update(user_id: int, data: dict):

        UserService.get_by_id(user_id)

        result = (
            supabase.table("users")
            .update(data)
            .eq("id", user_id)
            .execute()
        )

        return result.data[0]

    @staticmethod
    def delete(user_id: int):

        UserService.get_by_id(user_id)

        builds = (
            supabase.table("builds")
            .select("id")
            .eq("user_id", user_id)
            .execute()
        )

        if builds.data:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Cannot delete user because it has "
                    "associated builds. Delete them first."
                )
            )

        supabase.table("users") \
            .delete() \
            .eq("id", user_id) \
            .execute()

        return {
            "message": "User deleted"
        }

    @staticmethod
    def upload_picture(user_id, file):

        UserService.get_by_id(user_id)

        image_url = UploadService.upload_entity_picture(
            "users",
            user_id,
            file
        )

        supabase.table("users") \
            .update({"picture": image_url}) \
            .eq("id", user_id) \
            .execute()

        return {"picture": image_url}