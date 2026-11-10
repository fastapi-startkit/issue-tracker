from fastapi_startkit.fastapi import FastAPIProvider


class FastapiProvider(FastAPIProvider):
    def boot(self):
        super().boot()
        from routes.api import api, router

        self.app.fastapi.include_router(router.router)
        self.app.fastapi.include_router(api.router)
