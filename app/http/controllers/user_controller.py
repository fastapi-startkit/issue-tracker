from app.http.resources.user import UserResource
from app.models.user import User


class UserController:
    async def index(self) -> list[UserResource]:
        users = await User.order_by("name").get()
        return [UserResource.model_validate(user) for user in users]
