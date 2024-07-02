from sqlalchemy.orm import Session
from database.user import User
from schema.database.user import UserCreate, UserUpdate
from fastapi import HTTPException
from cryptography.fernet import Fernet
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def create(db: Session , user: UserCreate): # 建立使用者
    # hashed_password = get_password_hash(user.password)
    # db_user = User(**user.dict())
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user
    # ############################
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

def delete(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user

def verify_password(plain_password, hashed_password):
    """
    驗證密碼
    :param plain_password:
    :param hashed_password:
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """
    將密碼hash加密
    :param password:
    :return:
    """
    return pwd_context.hash(password)

def get_user(db: Session, username: str):
    return db.query(User).filter(User.user_name == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    user.is_login = True
    db.commit()
    db.refresh(user)
    return user
