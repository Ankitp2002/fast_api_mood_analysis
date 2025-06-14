from fastapi import APIRouter


def sub_router(module_name: str, tag: list = ["Auth"]) -> APIRouter:
    __router = APIRouter(prefix=f"/auth{module_name}", tags=tag)
    return __router


from . import auth  # noqa: E402
__routers: tuple[APIRouter, ...] = (auth.router,)
