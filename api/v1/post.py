from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import repository.post
from infrastructure.mysql import get_db
from schema.database.post import PostCreate, PostUpdate

router = APIRouter(
    tags=["post"],
    prefix="/posts"
)

# 取得全部
# [GET] /v1/posts
@router.get("/")
def list_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = repository.post.lists(db, skip=skip, limit=limit)
    return posts

#  新增
# [POST] /v1/posts
@router.post("/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):

    return repository.post.create(db=db, post=post)

# 取得特定
# [GET] /v1/posts/{id}
@router.get("/{item_id}")
def get_post(item_id: int,  db: Session = Depends(get_db)):
    return repository.post.get(db,item_id)
    # return "get_post"


# 更新特定
# [PUT] /v1/posts/{id}
@router.put("/{item_id}")
def  update_post(item_id: int,post_update: PostUpdate,db: Session = Depends(get_db)):
    return repository.post.update(db,item_id,post_update)

# 刪除特定
# [DELETE] /v1/posts/{id}
@router.delete("/{item_id}")
def delete_post(item_id: int, db: Session = Depends(get_db)):
    return repository.post.delete(db,item_id)