from typing import Annotated

from fastapi_startkit.validation import Field, FormRequest


class StoreProjectRequest(FormRequest):
    key: Annotated[str, Field().required().regex(r"^[A-Z]{2,10}$").unique("projects")]
    name: Annotated[str, Field().required().max(255)]
    description: str | None = None
