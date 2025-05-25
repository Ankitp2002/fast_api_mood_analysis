from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Start App...")
    yield
    print("Close App...")


class Server:
    def __init__(self):
        self._app = FastAPI(lifespan=lifespan)
        self._get_routers()

    @property
    def app(self):
        return self._app

    def _get_routers(self):
        from apis import __routers__
        for router in __routers__:
            self._app.include_router(router)
