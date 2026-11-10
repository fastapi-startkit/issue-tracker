from fastapi_startkit.masoniteorm.seeders import Seeder

from app.models.user import User


class UserTableSeeder(Seeder):
    async def run(self) -> None:
        await User.create({"name": "Ada Lovelace", "email": "ada@example.com"})
        await User.create({"name": "Grace Hopper", "email": "grace@example.com"})
        await User.create({"name": "Alan Turing", "email": "alan@example.com"})
