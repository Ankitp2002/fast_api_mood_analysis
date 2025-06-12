from fastapi import APIRouter
from apis.health.views import __routers as health_router

__routers__: tuple[APIRouter, ...] = (*health_router,)
