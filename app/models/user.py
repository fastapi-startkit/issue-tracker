from fastapi_startkit.masoniteorm.models import Model


class User(Model):
    id: int
    name: str
    email: str
