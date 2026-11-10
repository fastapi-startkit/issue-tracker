from app.http.controllers.issue_board_controller import IssueBoardController
from fastapi_startkit.fastapi import Router

board = IssueBoardController()

web = Router()
web.get("/projects/{project}/board", board.show, response_model=None)
web.post("/projects/{project}/board", board.store, response_model=None)
web.post("/issues/{issue}/transitions", board.transition, response_model=None)
web.delete("/issues/{issue}", board.destroy, response_model=None)
