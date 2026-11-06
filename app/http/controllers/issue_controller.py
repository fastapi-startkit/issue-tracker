from fastapi import Response
from fastapi_startkit.validation import Validated

from app.enums import IssueStatus
from app.http.requests.issue import StoreIssueRequest, TransitionIssueRequest, UpdateIssueRequest
from app.http.resources.issue import IssueDetailResource, IssueResource
from app.models.issue import Issue
from app.models.project import Project


class IssueController:
    async def index(self, project: int) -> list[IssueResource]:
        found = await Project.find_or_fail(project)
        issues = await Issue.with_("reporter", "assignee").where("project_id", found.id).order_by("number").get()
        return [IssueResource.model_validate(issue) for issue in issues]

    async def store(self, project: int, request: Validated[StoreIssueRequest], response: Response) -> IssueResource:
        found = await Project.find_or_fail(project)
        number = (await Issue.where("project_id", found.id).max("number") or 0) + 1
        issue = await Issue.create(
            {
                **request.model_dump(),
                "project_id": found.id,
                "number": number,
                "key": f"{found.key}-{number}",
                "status": IssueStatus.TODO,
            }
        )
        await issue.load("reporter", "assignee")
        response.status_code = 201
        return IssueResource.model_validate(issue)

    async def show(self, issue: int) -> IssueDetailResource:
        found = await Issue.with_("reporter", "assignee", "comments.author").find_or_fail(issue)
        return IssueDetailResource.model_validate(found)

    async def update(self, issue: int, request: Validated[UpdateIssueRequest]) -> IssueResource:
        found = await Issue.find_or_fail(issue)
        await found.update(request.model_dump(exclude_unset=True))
        await found.load("reporter", "assignee")
        return IssueResource.model_validate(found)

    async def transition(self, issue: int, request: Validated[TransitionIssueRequest]) -> IssueResource:
        found = await Issue.find_or_fail(issue)
        await found.update({"status": request.status})
        await found.load("reporter", "assignee")
        return IssueResource.model_validate(found)
