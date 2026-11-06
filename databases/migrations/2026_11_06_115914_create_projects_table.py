from fastapi_startkit.masoniteorm import Migration


class CreateProjectsTable(Migration):
    async def up(self):
        async with await self.schema.create("projects") as table:
            table.increments("id")
            table.string("key", 10).unique()
            table.string("name")
            table.text("description").nullable()
            table.timestamps()

    async def down(self):
        await self.schema.drop("projects")
