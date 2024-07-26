from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import repository.notify
from infrastructure.mysql import get_db
from schema.database.notify import NotifyCreate, NotifyUpdate

router = APIRouter(
    tags=["notify"],
    prefix="/notifies"
)


# 取得全部
# [GET] /v1/notifies
@router.get("/")
def list_notify(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notifies = repository.notify.lists(db, skip=skip, limit=limit)
    return notifies


# 新增
# [POST] /v1/notifies
@router.post("/")
def create_notify(notify: NotifyCreate, db: Session = Depends(get_db)):
    return repository.notify.create(db, notify)


# 取得特定
# [GET] /v1/notifies/{notify_id}
@router.get("/{notify_id}")
def get_notify(notify_id: int, db: Session = Depends(get_db)):
    notify = repository.notify.get(db, notify_id)
    return notify


# 更新特定
# [PUT] /v1/notifies/{notify_id}
@router.put("/{notify_id}")
def update_notify(notify_id: int, notify_update: NotifyUpdate, db: Session = Depends(get_db)):
    notify = repository.notify.update(db, notify_id, notify_update)
    return notify


# 刪除特定
# [DELETE] /v1/notifies/{notify_id}
@router.delete("/{notify_id}")
def delete_notify(notify_id: int, db: Session = Depends(get_db)):
    notify = repository.notify.delete(db, notify_id)
    return notify
