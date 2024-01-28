from fastapi import APIRouter

router = APIRouter(
    tags=["post"],
    prefix="/post"
)


@router.get("/")
def list_post():
    return {"status": "ok"}


@router.post("/")
def create_post():
    return {"status": "ok"}

