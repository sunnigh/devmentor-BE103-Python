from fastapi import APIRouter
from api.v1.post import router as post_router
from api.v1.notify import router as notify_router

from api.v1.event import router as event_router
from api.v1.user import router as user_router





routers = APIRouter()
router_list = [
    post_router,
    notify_router,
    user_router,
    event_router,
]

for router in router_list:
    routers.include_router(router)
