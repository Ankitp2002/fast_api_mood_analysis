from fastapi import APIRouter


def sub_router(module_name: str, tag: list = ["Health"]) -> APIRouter:
    __router = APIRouter(prefix=f"/health{module_name}", tags=tag)
    return __router


from . import health_check  # noqa: E402
__routers: tuple[APIRouter, ...] = (health_check.router,)
