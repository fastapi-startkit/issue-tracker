from typing import TYPE_CHECKING

from fastapi_startkit.masoniteorm.models import Model
from fastapi_startkit.masoniteorm.relationships import HasMany

if TYPE_CHECKING:
    from app.models.issue import Issue


class Project(Model):
    id: int
    key: str
    name: str
    description: str

    issues = HasMany["Issue"](local_key="id", foreign_key="project_id")
