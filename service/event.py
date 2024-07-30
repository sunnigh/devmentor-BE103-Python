from datetime import datetime
from sqlalchemy.orm import Session
from database.content import Content
from database.notifyservice import NotifyService
from database.sendlog import SendLog
from database.subscribes import Subscribe
from database.notify import Notify
from fastapi import HTTPException
from database.user import User
from repository.user import get as get_user_id
from utility.notify import send_email


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

        # 填入send_log table

        content = db.query(Content).filter(Content.event_id == event_id, Content.language == language).first()
        if not content:
            continue
        content_data = content.contents_data

        make_send_log(db, event_id, user_id, notification_type, datetime.now().date(), content_data)
        send_email(notification_data, username, content_data)

        info_list.append({"username": username, "content_data": content_data, "notification_data": notification_data})

    return {"info": info_list}


def trigger_log(event_id: int, db: Session):
    trigger_count = db.query(NotifyService).filter(NotifyService.event_id == event_id).count()
    if trigger_count is None:
        raise HTTPException(status_code=404, detail="Event not found")

    return {"Trigger times": trigger_count}


def make_send_log(db: Session,
                  event_id: int,
                  user_id: int,
                  notification_method: str,
                  date: datetime,
                  event_content: str):
    send_log = SendLog(
        event_id=event_id,
        user_id=user_id,
        notification_method=notification_method,
        date=date,
        event_content=event_content
    )
    db.add(send_log)
    db.commit()
    db.refresh(send_log)


def get_send_log(event_id: int, db: Session):
    send_times = db.query(SendLog).filter(SendLog.event_id == event_id).count()
    if send_times == 0:
        raise HTTPException(status_code=404, detail="No send logs found for this event")
    sendlogs = db.query(SendLog).filter(SendLog.event_id == event_id).all()
    if not sendlogs:
        return None
    sendlog_list = []
    for sendlog in sendlogs:
        sendlog_list.append({
            "event_id": sendlog.event_id,
            "user_id": sendlog.user_id,
            "notification_method": sendlog.notification_method,
            "date": sendlog.date,
            "event_content": sendlog.event_content,
        })
    return {
        "event_id": event_id,
        "total send times": send_times,
        "sendlog_list": sendlog_list
    }



