from app.http.controllers.home_controller import HomeController
from app.http.controllers.issue_controller import IssueController
from app.http.controllers.project_controller import ProjectController
from app.http.controllers.user_controller import UserController
from fastapi_startkit.fastapi import Router

controller = HomeController()
router = Router()
router.get("/", controller.index, response_model=None)
router.get("/health", controller.health)

issues = IssueController()

api = Router(prefix="/api")
api.resource("users", UserController, only=["index"])
api.resource("projects", ProjectController, only=["index", "store", "show"])
api.get("/projects/{project}/issues", issues.index)
api.post("/projects/{project}/issues", issues.store)
api.get("/issues/{issue}", issues.show)
