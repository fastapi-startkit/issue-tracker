from fastapi_startkit.masoniteorm.seeders import Seeder

from app.models.comment import Comment
from app.models.issue import Issue
from app.models.project import Project

ISSUES = [
    ("WEB", "Homepage hero image is blurry", "in_progress", "high", 1, 2),
    ("WEB", "Add a pricing page", "todo", "medium", 2, None),
    ("WEB", "Contact form sends two emails", "in_review", "urgent", 3, 1),
    ("WEB", "Update the footer links", "done", "low", 1, 3),
    ("WEB", "Translate the homepage", "todo", "low", 2, None),
    ("APP", "App crashes on launch on Android 12", "in_progress", "urgent", 3, 2),
    ("APP", "Dark mode for the settings screen", "todo", "medium", 1, 3),
]


class IssueTableSeeder(Seeder):
    async def run(self) -> None:
        for key, title, status, priority, reporter_id, assignee_id in ISSUES:
            project = await Project.where("key", key).first()
            issue = await project.add_issue(
                {"title": title, "priority": priority, "reporter_id": reporter_id, "assignee_id": assignee_id}
            )
            await issue.update({"status": status})

        first = await Issue.where("key", "WEB-1").first()
        await Comment.create({"issue_id": first.id, "author_id": 2, "body": "I can reproduce this on Safari."})
        await Comment.create({"issue_id": first.id, "author_id": 1, "body": "Thanks, swapping in a sharper image."})
