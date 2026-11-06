from fastapi import Response
from fastapi_startkit.validation import Validated

from app.http.requests.project import StoreProjectRequest
from app.http.resources.project import ProjectResource
from app.models.project import Project


class ProjectController:
    async def index(self) -> list[ProjectResource]:
        projects = await Project.order_by("key").get()
        return [ProjectResource.model_validate(project) for project in projects]

    async def store(self, request: Validated[StoreProjectRequest], response: Response) -> ProjectResource:
        project = await Project.create(request.model_dump())
        response.status_code = 201
        return ProjectResource.model_validate(project)

    async def show(self, project: int) -> ProjectResource:
        return ProjectResource.model_validate(await Project.find_or_fail(project))
