from typing import TYPE_CHECKING

from fastapi_startkit.masoniteorm.models import Model
from fastapi_startkit.masoniteorm.relationships import BelongsTo

if TYPE_CHECKING:
    from app.models.user import User


class Comment(Model):
    id: int
    issue_id: int
    author_id: int
    body: str

    author = BelongsTo["User"](local_key="author_id", foreign_key="id")
