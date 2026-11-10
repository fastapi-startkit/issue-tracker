from typing import Annotated

from fastapi_startkit.validation import Field, FormRequest

from app.enums import IssuePriority


class StoreIssueRequest(FormRequest):
    title: Annotated[str, Field().required().max(255)]
    description: str | None = None
    priority: IssuePriority = IssuePriority.MEDIUM
    reporter_id: Annotated[int, Field().required().exists("users", "id")]
    assignee_id: Annotated[int | None, Field().nullable().exists("users", "id")] = None
