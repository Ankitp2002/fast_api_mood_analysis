from fastapi import FastAPI
from contextlib import asynccontextmanager
from apis.reg_router import __routers__
from configuration.settings import get_settings
from configuration.db import init_db, close_db

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Start App...")
    await init_db(settings.DB_URL)

    yield
    print("Close App...")
    await close_db()


class Server:
    def __init__(self):
        self._app = FastAPI(lifespan=lifespan)
        self._setting = settings
        self._app.state.settings = self._setting
        self._get_routers()

    @property
    def app(self):
        return self._app

    def _get_routers(self):

        for router in __routers__:
            self._app.include_router(router)
