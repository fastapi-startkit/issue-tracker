from typing import Annotated

from fastapi_startkit.validation import Field, FormRequest, Validator
from pydantic import StringConstraints

from app.enums import IssuePriority, IssueStatus
from app.models.issue import Issue


class StoreIssueRequest(FormRequest):
    title: Annotated[str, Field().required().max(255)]
    description: str | None = None
    priority: IssuePriority = IssuePriority.MEDIUM
    reporter_id: Annotated[int, Field().required().exists("users", "id")]
    assignee_id: Annotated[int | None, Field().nullable().exists("users", "id")] = None


class IssueFilters(FormRequest):
    status: list[IssueStatus] = []
    priority: list[IssuePriority] = []
    assignee_id: int | None = None
    unassigned: bool = False
    q: Annotated[str, Field().max(100)] = ""
    sort: Annotated[str, Field().in_(["number", "-number", "updated_at", "-updated_at"])] = "-number"
    page: Annotated[int, Field().min(1)] = 1


class UpdateIssueRequest(FormRequest):
    title: Annotated[str, StringConstraints(min_length=1, max_length=255)] = ""
    description: str | None = None
    priority: IssuePriority = IssuePriority.MEDIUM
    assignee_id: Annotated[int | None, Field().nullable().exists("users", "id")] = None


class TransitionIssueRequest(FormRequest):
    status: IssueStatus

    @classmethod
    async def after(cls, validator: Validator) -> None:
        issue = await Issue.find(validator.context["issue"])
        status = validator.data.get("status")
        if issue is None or validator.errors.has("status"):
            return
        if not issue.status.can_move_to(status):
            validator.errors.add("status", f"An issue in {issue.status} can't move to {status}.")
