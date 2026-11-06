from dataclasses import dataclass

from fastapi_startkit.environment import env


@dataclass
class IssuesConfig:
    per_page: int = env("ISSUES_PER_PAGE", 20)
