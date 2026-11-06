# Issue Tracker

A Jira-style issue tracker API built with [fastapi-startkit](https://github.com/fastapi-startkit/fastapi-startkit).
It has projects, issues with a status workflow, assignees, priorities, comments and filtering.

This is the finished app from the [Build an Issue Tracker](https://fastapi-startkit.github.io/tutorials/issue-tracker/) tutorial.
Each lesson is one commit, tagged `lesson-02` to `lesson-10`, so you can compare your code with any step:

```bash
git checkout lesson-06
```

| Tag | Lesson |
|---|---|
| `lesson-02` | Create the project |
| `lesson-03` | Users and projects |
| `lesson-04` | The projects API |
| `lesson-05` | Issues |
| `lesson-06` | The status workflow |
| `lesson-07` | Assignees and priorities |
| `lesson-08` | Comments |
| `lesson-09` | Filtering and pagination |
| `lesson-10` | Testing |

## Run it

```bash
uv sync
cp .env.example .env
uv run python artisan db:migrate
uv run python artisan db:seed
uv run python artisan serve
```

Then open http://127.0.0.1:8000/docs or try:

```bash
curl -s "http://127.0.0.1:8000/api/projects/1/issues?status=in_progress"
```

## Test it

```bash
echo "DB_DATABASE=databases/testing.sqlite" > .env.testing
uv run pytest
```
