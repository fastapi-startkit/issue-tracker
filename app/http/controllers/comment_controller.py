from fastapi import Response
from fastapi_startkit.validation import Validated

from app.http.requests.comment import StoreCommentRequest
from app.http.resources.comment import CommentResource
from app.models.comment import Comment
from app.models.issue import Issue


class CommentController:
    async def index(self, issue: int) -> list[CommentResource]:
        found = await Issue.find_or_fail(issue)
        comments = await Comment.with_("author").where("issue_id", found.id).order_by("id").get()
        return [CommentResource.model_validate(comment) for comment in comments]

    async def store(self, issue: int, request: Validated[StoreCommentRequest], response: Response) -> CommentResource:
        found = await Issue.find_or_fail(issue)
        comment = await Comment.create({**request.model_dump(), "issue_id": found.id})
        await comment.load("author")
        response.status_code = 201
        return CommentResource.model_validate(comment)
