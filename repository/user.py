from sqlalchemy.orm import Session
from database.user import User
from schema.database.user import UserCreate, UserUpdate
from fastapi import HTTPException
from cryptography.fernet import Fernet
from service.user import get_password_hash


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create(db: Session , user: UserCreate): # 建立使用者
    hashed_password = get_password_hash(user.password)
    db_user = User(
        user_name=user.user_name,
        account=user.account,
        password=hashed_password,
        is_login=False,
        language=user.language,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get(db: Session, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

def update(db: Session, user_id: int, user_update: UserUpdate):
    db_user = get(db, user_id)
    if not db_user.is_login:
        raise HTTPException(status_code=403, detail="User is not log in")

    db_user.password = get_password_hash(user_update.password)
    db_user.user_name = user_update.user_name
    db_user.language = user_update.language

    db.commit()
    db.refresh(db_user)
    return db_user

def delete(db: Session, user_id: int):
    db_user = get(db, user_id)
    db.delete(db_user)
    db.commit()
    return db_user

def get_user(db: Session, username: str):
    return db.query(User).filter(User.user_name == username).first()


