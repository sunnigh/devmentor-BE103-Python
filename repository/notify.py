from sqlalchemy.orm import Session
from database.notify import Notify
from schema.database.notify import NotifyCreate, NotifyUpdate
from fastapi import HTTPException

def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Notify).offset(skip).limit(limit).all()

def create(db: Session, notify: NotifyCreate):
    db_notify = Notify(**notify.dict())
    db.add(db_notify)
    db.commit()
    db.refresh(db_notify)
    return db_notify

def get(db: Session, notify_id: int):
    return db.query(Notify).filter(Notify.id == notify_id).first()

def update(db: Session, notify_id: int, notify_update: NotifyUpdate):
    db_notify = get(db,id)
    if not db_notify:
        raise HTTPException(status_code=404, detail="Notification Method not found")
    for key, value in notify_update.dict().items():
        setattr(db_notify, key, value)
    db.commit()
    db.refresh(db_notify)
    return db_notify

def delete(db: Session, notify_id: int):
    db_notify = get(db,id)
    if not db_notify:
        raise HTTPException(status_code=404, detail="Notification Method not found")
    db.delete(db_notify)
    db.commit()
    return {"message": "Notification Method deleted successfully"}