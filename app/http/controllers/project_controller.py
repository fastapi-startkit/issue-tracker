class ProjectController:
    async def index(self):
        return [
            {"id": 1, "key": "WEB", "name": "Website"},
            {"id": 2, "key": "APP", "name": "Mobile app"},
        ]
