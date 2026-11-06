from pydantic import BaseModel, ConfigDict


class ProjectResource(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    key: str
    name: str
    description: str | None
