from fastapi import APIRouter

from api.general.index import router as index_router

routers = APIRouter()
router_list = [
    index_router,
]

for router in router_list:
    routers.include_router(router)
