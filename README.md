# Issue Tracker

A Jira-style issue tracker built with [fastapi-startkit](https://github.com/fastapi-startkit/fastapi-startkit).
It has projects, issues with a status workflow, assignees, priorities, comments, filtering and a Vue issue board.

This is the finished app from the [Build an Issue Tracker](https://fastapi-startkit.github.io/tutorials/issue-tracker/) course.
Each lesson that changes code is one commit, tagged `lesson-02` to `lesson-13`, so you can compare your code with any step:

```bash
git checkout lesson-07
```

| Tag | Lesson |
|---|---|
| `lesson-02` | Creating the project |
| `lesson-03` | A tour of the project |
| `lesson-04` | Routes and controllers |
| `lesson-05` | Users and projects |
| `lesson-06` | The projects API |
| `lesson-07` | Issues |
| `lesson-08` | The status workflow |
| `lesson-09` | Editing and deleting issues |
| `lesson-10` | Comments and eager loading |
| `lesson-11` | Filtering and pagination |
| `lesson-12` | An issue board with Inertia |
| `lesson-13` | Testing |

## Run it

```bash
uv sync
cp .env.example .env
uv run python artisan db:migrate
uv run python artisan db:seed
npm install
npm run build
uv run python artisan serve
```

Then open http://127.0.0.1:8000/projects/1/board, or try the API:

```bash
curl -s "http://127.0.0.1:8000/api/projects/1/issues?status=in_progress"
```

## Test it

```bash
echo "DB_DATABASE=databases/testing.sqlite" > .env.testing
uv run pytest
```

The board test reads the built frontend, so run `npm run build` first.
