from sqlalchemy.orm import Session
from database.user import User
from schema.database.user import UserCreate, UserUpdate
from fastapi import HTTPException
from cryptography.fernet import Fernet


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
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user_update.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


