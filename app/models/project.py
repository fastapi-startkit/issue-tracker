from fastapi_startkit.masoniteorm.models import Model
from fastapi_startkit.masoniteorm.relationships import HasMany

from app.enums import IssueStatus
from app.models.issue import Issue


class Project(Model):
    id: int
    key: str
    name: str
    description: str

    issues = HasMany[Issue](local_key="id", foreign_key="project_id")

    async def add_issue(self, attributes: dict) -> Issue:
        number = (await Issue.where("project_id", self.id).max("number") or 0) + 1
        return await Issue.create(
            {
                **attributes,
                "project_id": self.id,
                "number": number,
                "key": f"{self.key}-{number}",
                "status": IssueStatus.TODO,
            }
        )
