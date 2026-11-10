from fastapi_startkit.inertia import Inertia, InertiaRedirect
from fastapi_startkit.inertia.inertia import InertiaResponse
from fastapi_startkit.validation import Validated

from app.http.requests.issue import StoreIssueRequest, TransitionIssueRequest
from app.http.resources.issue import IssueResource
from app.http.resources.project import ProjectResource
from app.http.resources.user import UserResource
from app.models.issue import Issue
from app.models.project import Project
from app.models.user import User


class IssueBoardController:
    async def show(self, project: int) -> InertiaResponse:
        found = await Project.find_or_fail(project)
        issues = await Issue.with_("reporter", "assignee").where("project_id", found.id).order_by("number").get()
        users = await User.order_by("name").get()
        return Inertia.render("Issues/Board", {
            "project": ProjectResource.model_validate(found).model_dump(mode="json"),
            "issues": [IssueResource.model_validate(issue).model_dump(mode="json") for issue in issues],
            "users": [UserResource.model_validate(user).model_dump(mode="json") for user in users],
        })

    async def store(self, project: int, request: Validated[StoreIssueRequest]) -> InertiaRedirect:
        found = await Project.find_or_fail(project)
        await found.add_issue(request.model_dump())
        return Inertia.redirect(f"/projects/{found.id}/board")

    async def transition(self, issue: int, request: Validated[TransitionIssueRequest]) -> InertiaRedirect:
        found = await Issue.find_or_fail(issue)
        await found.update({"status": request.status})
        return Inertia.redirect(f"/projects/{found.project_id}/board")

    async def destroy(self, issue: int) -> InertiaRedirect:
        found = await Issue.find_or_fail(issue)
        await found.delete()
        return Inertia.redirect(f"/projects/{found.project_id}/board")
