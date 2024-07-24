from sqlalchemy.orm import Session
from database.content import Content
from database.notifyservice import NotifyService
from database.subscribes import Subscribe
from database.notify import Notify
from fastapi import HTTPException
from database.user import User
from repository.user import get as get_user_id
from utility.auth import send_email


def trigger_event(db: Session, event_id: int, notification_type: str):
    subscriptions = db.query(Subscribe).filter(Subscribe.event_id == event_id).all()
    if not subscriptions:
        raise HTTPException(status_code=404, detail="No subscriptions found for this event")

    info_list = []

    for subscription in subscriptions:
        user_id = subscription.user_id
        user = get_user_id(db, user_id)
        if not user:
            continue
        username = user.user_name
        language = user.language

        notification_method = db.query(Notify).filter(Notify.user_id == user_id,
                                                      Notify.type == notification_type).first()
        if not notification_method:
            continue
        notification_data = notification_method.data
        notification_method_id = notification_method.id

        db_notify_service = NotifyService(event_id=event_id, notification_method_id=notification_method_id)
        db.add(db_notify_service)
        db.commit()
        db.refresh(db_notify_service)

        content = db.query(Content).filter(Content.event_id == event_id, Content.language == language).first()
        if not content:
            continue
        content_data = content.contents_data

        send_email(notification_data, username, content_data)

        info_list.append({"username": username, "content_data": content_data, "notification_data": notification_data})

    return {"info": info_list}
