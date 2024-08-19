from sqlalchemy.orm import Session
from database.user import User
from schema.database.user import UserCreate, UserUpdate, User as PUser
from fastapi import HTTPException, Depends

from utility.auth import get_password_hash


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create(db: Session, user: UserCreate):  # 建立使用者
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
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


def update(db: Session, user_id: int, user_update: UserUpdate, current_user: PUser):
    db_user = get(db, user_id)
    if db_user.user_name != current_user.user_name:
        raise HTTPException(status_code=403, detail="Not authorized")
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


def get_by_account(db: Session, account: str):
    user = db.query(User).filter(User.account == account).first()
    if user:
        raise HTTPException(status_code=400, detail="Account already exists")
    return user


def get_by_password(db: Session, password: str):
    user_with_same_password = db.query(User).filter(User.password == password).first()
    if user_with_same_password:
        raise HTTPException(status_code=400, detail="Password is already in use")
    return user_with_same_password
