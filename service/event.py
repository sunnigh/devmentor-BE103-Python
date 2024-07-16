from repository.event import create as create_event ,delete as delete_event
from repository.event import subscribe
from repository.notify import get as get_notify
from repository.user import get as get_user


def reserve_course():
    create_event(db, EventCreate)
    user = get_user(db, current_user.user_id)
    if user.language == "enus":
        content = get_content(contents_id)
        return content
    notify = get_notify(db, notification_method_id)
    #DB_notifyservice create
    notify_implement(notify.type, content.contents_data)
    subscription = subscribe(db, event_id, subscribed_event,current_user)
    #DB_subscribe create
    return


def cancel_course():
    delete_event(db, event_id)
    user = get_user(db, current_user.user_id)
    if user.language == "enus":
        content = get_content(contents_id)
    notify = get_notify(db, notification_method_id)
    notify_implement(notify.type,content.contents_data)
    subscription = cancel_subscribe(db, event_id, subscribed_event,current_user)
    return


