from fastapi_startkit.masoniteorm.seeders import Seeder

from databases.seeders.issue_table_seeder import IssueTableSeeder
from databases.seeders.project_table_seeder import ProjectTableSeeder
from databases.seeders.user_table_seeder import UserTableSeeder


class DatabaseSeeder(Seeder):
    async def run(self):
        await self.call(UserTableSeeder, ProjectTableSeeder, IssueTableSeeder)
