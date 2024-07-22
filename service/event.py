from sqlalchemy.orm import Session
from database.content import Content
from database.event import Event
from database.notifyservice import NotifyService
from database.subscribes import Subscribe
from database.user import User
from database.notify import Notify
from repository.event import create_notify_service
from schema.database.event import EventCreate, EventUpdate, EventSubscribe
from fastapi import HTTPException
from repository.user import get as get_user


def trigger_event(db, event_id, notification_type: str):
    subscriptions = db.query(Subscribe).filter(Subscribe.event_id == event_id).all()
    if not subscriptions:
        return HTTPException(status_code=404, detail="No subscriptions found for this event")

    user_ids = [subscriptions.user_id for subscription in subscriptions]
    for user_id in user_ids:
        user = get_user(db, user_id)
        if not user:
            continue
        username = user.user_name
        language = user.language

    notification_method = db.query(Notify).filter(Notify.user_id == user_id, Notify.type == notification_type).first()
    if not notification_method:
        return
    notification_data = notification_method.data
    notification_method_id = notification_method.id

    create_notify_service(db, event_id, notification_method_id)

    return None