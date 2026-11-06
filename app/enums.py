from enum import StrEnum


class IssueStatus(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    DONE = "done"

    def transitions(self) -> list["IssueStatus"]:
        return WORKFLOW[self]

    def can_move_to(self, status: "IssueStatus") -> bool:
        return status in self.transitions()


WORKFLOW = {
    IssueStatus.TODO: [IssueStatus.IN_PROGRESS],
    IssueStatus.IN_PROGRESS: [IssueStatus.TODO, IssueStatus.IN_REVIEW],
    IssueStatus.IN_REVIEW: [IssueStatus.IN_PROGRESS, IssueStatus.DONE],
    IssueStatus.DONE: [IssueStatus.TODO],
}


class IssuePriority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"
