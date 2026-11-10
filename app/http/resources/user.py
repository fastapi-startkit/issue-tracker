from pydantic import BaseModel, ConfigDict


class UserResource(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
