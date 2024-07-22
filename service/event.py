from typing import List

from sqlalchemy.orm import Session
from database.content import Content
from database.event import Event
from database.notifyservice import NotifyService
from database.subscribes import Subscribe
from database.user import User
from database.notify import Notify
from repository.event import create_notify_service, get_content_by_event_and_language
from schema.database.event import EventCreate, EventUpdate, EventSubscribe
from schema.database.user import User as PUser
from fastapi import HTTPException
from repository.user import get as get_user


def trigger_event(db, event_id, notification_type: str):
    subscriptions = db.query(Subscribe).filter(Subscribe.event_id == event_id).all()
    if not subscriptions:
        return HTTPException(status_code=404, detail="No subscriptions found for this event")

    info_list = []
    user_ids = [subscriptions.user_id for subscription in subscriptions]
    for user_id in user_ids:
        user = get_user(db, user_id)
        if not user:
            continue
        username = user.user_name
        language = user.language

    notification_method = db.query(Notify).filter(Notify.user_id == user_id, Notify.type == notification_type).first()
    notification_data = notification_method.data
    notification_method_id = notification_method.id

    create_notify_service(db, event_id, notification_method_id)

    content = db.query(Content).filter(Content.event_id == event_id, Content.language == language).first()
    content_data = content.contents_data

    info_list.append({"username": username, "content_data": content_data, "notification_type": notification_type})

    return {"info": info_list}
