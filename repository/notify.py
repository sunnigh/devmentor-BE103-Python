from sqlalchemy.orm import Session
from database.notify import Notify
from schema.database.notify import NotifyCreate, NotifyUpdate
from fastapi import HTTPException


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notify).offset(skip).limit(limit).all()


def create(db: Session, notify: NotifyCreate):
    db_notify = Notify(
        type=notify.type,
        data=notify.data,
        user_id=notify.user_id
    )
    db.add(db_notify)
    db.commit()
    db.refresh(db_notify)
    return db_notify


def get(db: Session, notify_id: int):
    return db.query(Notify).filter(Notify.id == notify_id).first()


def update(db: Session, notify_id: int, notify_update: NotifyUpdate):
    db_notify = get(db, notify_id)
    if not db_notify:
        raise HTTPException(status_code=404, detail="Notification Method not found")
    db_notify.type = notify_update.type
    db_notify.data = notify_update.data
    db_notify.user_id = notify_update.user_id
    db.commit()
    db.refresh(db_notify)
    return db_notify


def delete(db: Session, notify_id: int):
    db_notify = get(db, notify_id)
    if not db_notify:
        raise HTTPException(status_code=404, detail="Notification Method not found")
    db.delete(db_notify)
    db.commit()
    return {"message": "Notification Method deleted successfully"}
