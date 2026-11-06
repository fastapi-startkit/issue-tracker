from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.http.resources.user import UserResource


class CommentResource(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    body: str
    author: UserResource
    created_at: datetime
