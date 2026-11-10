from fastapi_startkit.masoniteorm import Migration


class CreateCommentsTable(Migration):
    async def up(self):
        async with await self.schema.create("comments") as table:
            table.increments("id")
            table.integer("issue_id").unsigned()
            table.foreign("issue_id").references("id").on("issues").on_delete("cascade")
            table.integer("author_id").unsigned()
            table.foreign("author_id").references("id").on("users")
            table.text("body")
            table.timestamps()

    async def down(self):
        await self.schema.drop("comments")
