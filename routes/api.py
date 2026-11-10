from app.http.controllers.home_controller import HomeController
from app.http.controllers.project_controller import ProjectController
from fastapi_startkit.fastapi import Router

controller = HomeController()
router = Router()
router.get("/", controller.index, response_model=None)
router.get("/health", controller.health)

api = Router(prefix="/api")
api.resource("projects", ProjectController, only=["index"])
