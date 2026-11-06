from typing import Annotated

from fastapi_startkit.validation import Field, FormRequest


class StoreCommentRequest(FormRequest):
    author_id: Annotated[int, Field().required().exists("users", "id")]
    body: Annotated[str, Field().required().max(5000)]
