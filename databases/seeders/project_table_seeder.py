from fastapi_startkit.masoniteorm.seeders import Seeder

from app.models.project import Project


class ProjectTableSeeder(Seeder):
    async def run(self) -> None:
        await Project.create({"key": "WEB", "name": "Website", "description": "The marketing site"})
        await Project.create({"key": "APP", "name": "Mobile app"})
