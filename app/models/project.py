from fastapi_startkit.masoniteorm.models import Model


class Project(Model):
    id: int
    key: str
    name: str
    description: str
