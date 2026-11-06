from fastapi_startkit.fastapi.testing import HttpTestCase
from fastapi_startkit.masoniteorm.testing import RefreshDatabase

from app.models.issue import Issue
from app.models.project import Project
from app.models.user import User


class TestIssues(RefreshDatabase, HttpTestCase):
    def get_application(self):
        from bootstrap.application import app

        return app

    async def make_issue(self, **attributes) -> Issue:
        project = await Project.create({"key": "WEB", "name": "Website"})
        reporter = await User.create({"name": "Ada", "email": "ada@example.com"})
        response = await self.post(
            f"/api/projects/{project.id}/issues", json={"title": "Fix it", "reporter_id": reporter.id, **attributes}
        )
        return await Issue.find_or_fail(response.json()["id"])

    async def test_it_numbers_issues_per_project(self):
        first = await self.make_issue()
        response = await self.post(
            f"/api/projects/{first.project_id}/issues", json={"title": "Second", "reporter_id": first.reporter_id}
        )

        response.assert_created().assert_json(lambda json: json.where("key", "WEB-2").where("status", "todo").etc())

    async def test_it_rejects_an_unknown_assignee(self):
        project = await Project.create({"key": "WEB", "name": "Website"})
        reporter = await User.create({"name": "Ada", "email": "ada@example.com"})

        response = await self.post(
            f"/api/projects/{project.id}/issues", json={"title": "Fix it", "reporter_id": reporter.id, "assignee_id": 99}
        )

        response.assert_status(422).assert_json_structure({"errors": ["assignee_id"]})

    async def test_it_follows_the_workflow(self):
        issue = await self.make_issue()

        (await self.post(f"/api/issues/{issue.id}/transitions", json={"status": "in_progress"})).assert_ok()
        (await self.post(f"/api/issues/{issue.id}/transitions", json={"status": "in_review"})).assert_ok()

        response = await self.post(f"/api/issues/{issue.id}/transitions", json={"status": "todo"})
        response.assert_status(422).assert_json_structure({"errors": ["status"]})

    async def test_it_comments_on_an_issue(self):
        issue = await self.make_issue()

        response = await self.post(
            f"/api/issues/{issue.id}/comments", json={"author_id": issue.reporter_id, "body": "On it"}
        )

        response.assert_created()
        (await self.get(f"/api/issues/{issue.id}")).assert_json(
            lambda json: json.count("comments", 1).where("comments.0.body", "On it").etc()
        )

    async def test_it_filters_by_status(self):
        issue = await self.make_issue()
        await self.post(f"/api/projects/{issue.project_id}/issues", json={"title": "Other", "reporter_id": issue.reporter_id})
        await self.post(f"/api/issues/{issue.id}/transitions", json={"status": "in_progress"})

        response = await self.get(f"/api/projects/{issue.project_id}/issues?status=in_progress")

        response.assert_ok().assert_json(
            lambda json: json.where("total", 1).where("data.0.key", "WEB-1").etc()
        )
