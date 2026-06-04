import uuid

from fastapi import UploadFile

from app.database.supabase_client import supabase
from app.config.settings import settings


class UploadService:

    @staticmethod
    def upload_entity_picture(
        folder: str,
        entity_id: int,
        file: UploadFile
    ):
        extension = file.filename.split(".")[-1]

        filename = (
            f"{folder}/{entity_id}/"
            f"{uuid.uuid4()}.{extension}"
        )

        supabase.storage \
            .from_(settings.SUPABASE_BUCKET) \
            .upload(
                filename,
                file.file.read()
            )

        return (
            supabase.storage
            .from_(settings.SUPABASE_BUCKET)
            .get_public_url(filename)
        )