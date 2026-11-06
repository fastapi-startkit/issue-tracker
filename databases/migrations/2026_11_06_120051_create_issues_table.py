from fastapi_startkit.masoniteorm import Migration


class CreateIssuesTable(Migration):
    async def up(self):
        async with await self.schema.create("issues") as table:
            table.increments("id")
            table.integer("project_id").unsigned()
            table.foreign("project_id").references("id").on("projects").on_delete("cascade")
            table.integer("number").unsigned()
            table.string("key", 20).unique()
            table.string("title")
            table.text("description").nullable()
            table.string("status", 20).default("todo")
            table.string("priority", 20).default("medium")
            table.integer("reporter_id").unsigned()
            table.foreign("reporter_id").references("id").on("users")
            table.integer("assignee_id").unsigned().nullable()
            table.foreign("assignee_id").references("id").on("users").on_delete("set null")
            table.timestamps()
            table.unique(["project_id", "number"])

    async def down(self):
        await self.schema.drop("issues")
