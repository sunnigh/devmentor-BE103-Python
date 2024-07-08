from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import repository.event
from infrastructure.mysql import get_db
from schema.database.event import EventCreate, EventUpdate, EventSubscribe

router = APIRouter(
    tags=["event"],
    prefix="/events"
)


# 取得全部
# [GET] /v1/events
@router.get("/")
def list_event(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = repository.event.lists(db, skip=skip, limit=limit)
    return events


# 新增
# [POST] /v1/events
@router.post("/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    return repository.event.create(db=db, event=event)


# 取得特定
# [GET] /v1/events/{event_id}
@router.get("/{event_id}")
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = repository.event.get(db, event_id)
    return event


# 更新特定
# [PUT] /v1/events/{event_id}
@router.put("/{event_id}")
def update_event(event_id: int, event_update: EventUpdate, db: Session = Depends(get_db)):
    event = repository.event.update(db, event_id, event_update)

    return event


# 刪除特定
# [DELETE] /v1/events/{event_id}
@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = repository.event.delete(db, event_id)
    return event


@router.post("/{event_id}/subscribe")
def subscribe_event(event_id: int, subscribe: EventSubscribe, db: Session = Depends(get_db),
                    token: str = Depends(oauth2_scheme)):
    return repository.event.subscribe(db, event_id, subscribe, token)
