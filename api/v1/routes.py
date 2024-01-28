from fastapi import APIRouter
from api.v1.post import router as post_router


routers = APIRouter()
router_list = [
    post_router
]

for router in router_list:
    routers.include_router(router)
