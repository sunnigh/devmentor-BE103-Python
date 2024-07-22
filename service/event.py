from sqlalchemy.orm import Session
from database.content import Content
from database.notifyservice import NotifyService
from database.subscribes import Subscribe
from database.notify import Notify
from fastapi import HTTPException
from database.user import User
from repository.user import get as get_user_id


def trigger_event(db: Session, event_id: int, notification_type: str):
    subscriptions = db.query(Subscribe).filter(Subscribe.event_id == event_id).all()
    print("subscriptions is here", subscriptions)
    if not subscriptions:
        raise HTTPException(status_code=404, detail="No subscriptions found for this event")

    user_ids = [subscription.user_id for subscription in subscriptions]
    print("user ids here", user_ids)
    info_list = []

    for user_id in user_ids:
        user = get_user_id(db, user_id)
        if not user:
            print(f"User with id {user_id} not found.")
            continue
        username = user.user_name
        language = user.language
        print("language", language)

        notification_method = db.query(Notify).filter(Notify.user_id == user_id,
                                                      Notify.type == notification_type).first()
        print("notification_method is here", notification_method)
        if not notification_method:
            print(f"No notification method found for user_id {user_id} and type {notification_type}")
            continue
        notification_data = notification_method.data
        notification_method_id = notification_method.id

        db_notify_service = NotifyService(event_id=event_id, notification_method_id=notification_method_id)
        db.add(db_notify_service)
        db.commit()
        db.refresh(db_notify_service)

        content = db.query(Content).filter(Content.event_id == event_id, Content.language == language).first()
        if not content:
            print(f"No content found for event_id {event_id} and language {language}")
            continue
        content_data = content.contents_data
        print("content_data", content_data)

        info_list.append({"username": username, "content_data": content_data, "notification_type": notification_type})

    return {"info": info_list}
