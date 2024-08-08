from sqlalchemy.orm import Session
from database.content import Content
from database.event import Event
from database.notifyservice import NotifyService
from database.subscribes import Subscribe
from schema.database.event import EventCreate, EventUpdate, EventSubscribe
from fastapi import HTTPException, Depends
from schema.database.user import User

from service.user import oauth2_scheme


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()


def create(db: Session, event: EventCreate):
    db_event = Event(event_date=event.date)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get(db: Session, event_id: int):
    return db.query(Event).filter(Event.id == event_id).first()


def update(db: Session, event_id: int, event_update: EventUpdate):
    db_event = get(db, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db_event.date = event_update.date
    db.commit()
    db.refresh(db_event)
    return db_event


def delete(db: Session, event_id: int):
    db_event = get(db, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(db_event)
    db.commit()
    return db_event


def subscribe(db: Session, event_id: int, current_user: User):
    db_event = get(db, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")

    existing_subscription = (db.query(Subscribe).
                             filter_by(event_id=event_id, user_id=current_user.id).first())
    if existing_subscription:
        raise HTTPException(status_code=400, detail="Already subscribed to this event")

    db_subscription = Subscribe(event_id=event_id, user_id=current_user.id)
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


def cancel_subscribe(db: Session, event_id: int, current_user: User):
    subscription = db.query(Subscribe).filter_by(event_id=event_id, user_id=current_user.id).first()
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")

    db.delete(subscription)
    db.commit()
    return subscription


def get_content_by_event_and_language(db: Session, event_id: int, language: str, current_user: User):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    content = db.query(Content).filter(Content.event_id == event_id, Content.language == language).first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"contents_data": content.contents_data}


def create_content(db: Session, event_id: int, language: str, contents_data: str, current_user: User):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    db_content = Content(event_id=event_id, language=language, contents_data=contents_data)
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return {"message": "Content POST successfully"}


def create_notify_service(db: Session, event_id: int, notification_method_id: int):
    db_notify_service = NotifyService(event_id=event_id, notification_method_id=notification_method_id)
    db.add(db_notify_service)
    db.commit()
    db.refresh(db_notify_service)
    return {"message": "NotifyService POST successfully"}


def get_notify_service(db: Session, event_id: int):
    notify_services = (db.query(NotifyService).
                       filter(NotifyService.event_id == event_id).all())
    if not notify_services:
        raise HTTPException(status_code=404, detail="NotifyService not found")
    notification_method_ids = [service.notification_method_id for service in notify_services]
    return {"notification_method_id": notification_method_ids}


def list_event(db: Session, skip: int = 0, limit: int = 100):
    events = lists(db, skip, limit)
    event_contents = []
    for event in events:
        contents = db.query(Content).filter(Content.event_id == event.id).all()
        event_contents.append({"event": event, "contents": contents})
    return event_contents


def update_content(db, event_id, language, contents_data, current_user):
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    db_content = db.query(Content).filter_by(event_id=event_id, language=language).first()
    db_content.contents_data = contents_data
    db.commit()
    db.refresh(db_content)
    return {"message": "Content updated successfully", "content": contents_data}
