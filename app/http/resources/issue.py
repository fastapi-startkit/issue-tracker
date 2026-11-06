from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.enums import IssuePriority, IssueStatus
from app.http.resources.user import UserResource


class IssueResource(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    key: str
    title: str
    description: str | None
    status: IssueStatus
    priority: IssuePriority
    reporter: UserResource
    assignee: UserResource | None
    created_at: datetime
