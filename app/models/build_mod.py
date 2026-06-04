from pydantic import BaseModel


class BuildModCreate(BaseModel):
    build_id: int
    mod_id: int


class BuildModResponse(BaseModel):
    id: int
    build_id: int
    mod_id: int

    model_config = {
        "from_attributes": True
    }