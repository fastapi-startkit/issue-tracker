from typing import TYPE_CHECKING

from fastapi_startkit.masoniteorm.models import Model
from fastapi_startkit.masoniteorm.relationships import BelongsTo, HasMany

from app.enums import IssuePriority, IssueStatus

if TYPE_CHECKING:
    from app.models.comment import Comment
    from app.models.project import Project
    from app.models.user import User


class Issue(Model):
    id: int
    project_id: int
    number: int
    key: str
    title: str
    description: str
    status: IssueStatus
    priority: IssuePriority
    reporter_id: int
    assignee_id: int | None

    project = BelongsTo["Project"](local_key="project_id", foreign_key="id")
    reporter = BelongsTo["User"](local_key="reporter_id", foreign_key="id")
    assignee = BelongsTo["User"](local_key="assignee_id", foreign_key="id")
    comments = HasMany["Comment"](local_key="id", foreign_key="issue_id")
