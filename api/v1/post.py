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


@router.delete("/{post_id}")
def delete_post(post_id: str):
    return {"status": "ok"}


@router.put("/{post_id}")
def update_post(post_id: str):
    return {"status": "ok"}
