from service.event import trigger_event, trigger_log, get_send_log
from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
import repository.event
from infrastructure.mysql import get_db
from schema.database.event import EventCreate, EventUpdate, EventSubscribe, EventTriggerRequest
from service.user import get_current_user
from schema.database.user import User

router = APIRouter(
    tags=["event"],
    prefix="/events"
)


# 取得全部
# [GET] /v1/events
@router.get("/")
def list_event(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = repository.event.list_event(db, skip=skip, limit=limit)
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
def subscribe_event(event_id: int,
                    db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)
                    ):
    return repository.event.subscribe(db, event_id, current_user)


@router.delete("/{event_id}/subscribe")
def cancel_subscribe_event(
        event_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    return repository.event.cancel_subscribe(db, event_id, current_user)


# 取得內容 event_id & language 到contents找資料
@router.get("/{event_id}/lang/{language}")
def get_content(event_id: int,
                language: str,
                db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)
                ):
    return repository.event.get_content_by_event_and_language(db, event_id, language, current_user)


# 更新內容寫入event_id & language &content_data
@router.post("/{event_id}/lang/{language}")
def post_content(event_id: int,
                 language: str,
                 contents_data: str = Form(...),
                 db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)
                 ):
    return repository.event.create_content(db, event_id, language, contents_data, current_user)


# 新增 notify_service
@router.post("/{event_id}/notify/{notification_method_id}")
def create_notify_service(event_id: int, notification_method_id: int, db: Session = Depends(get_db)):
    return repository.event.create_notify_service(db, event_id, notification_method_id)


# 取得 notify_service
@router.get("/{event_id}/notify")
def get_notify_service(event_id: int, db: Session = Depends(get_db)):
    return repository.event.get_notify_service(db, event_id)


@router.post("/{event_id}/trigger")
def trigger(event_id: int, notification: EventTriggerRequest, db: Session = Depends(get_db)):
    return trigger_event(db, event_id, notification.type)


@router.get("/{event_id}/trigger")
def get_trigger_log(event_id: int, db: Session = Depends(get_db)):
    return trigger_log(event_id, db)


@router.get("/{event_id}/sendlog")
def send_log(event_id: int, db: Session = Depends(get_db)):
    return get_send_log(event_id, db)


@router.put("/{event_id}/lang/{language}")
def update_content(event_id: int,
                   language: str,
                   contents_data: str = Form(...),
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    return repository.event.update_content(db, event_id, language, contents_data, current_user)
