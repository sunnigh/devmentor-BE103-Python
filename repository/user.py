from sqlalchemy.orm import Session
from database.user import User
from schema.database.user import UserCreate, UserUpdate
from fastapi import HTTPException
from cryptography.fernet import Fernet
# from passlib.context import cryptography

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# def create(db: Session, user: UserCreate): # 建立使用者
    # db_user = User(**user.dict())
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user
    ############################
    # hashed_password = get_password_hash(user.password)
    # db_user = User(
    #     username=user.username,
    #     account=user.email,
    #     password=hashed_password,
    #     is_login=False,
    #     language=user.language,
    #     )
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user

def get(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
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
    return db.query(models.User).filter(models.User.username == username).first()

# def authenticate_user(db: Session, username: str, password: str):
#     user = get_user(db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user

def encrypt_password(password: str) -> str:
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password: str) -> str:
    return fernet.decrypt(encrypted_password.encode()).decode()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not decrypt_password(user.hashed_password) == password:
        return False
    return user

def create(db: Session, user: UserCreate): # 建立使用者
    # db_user = User(**user.dict())
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user
    hashed_password = encrypt_password(user.password)
    db_user = User(
        username=user.username,
        account=user.email,
        password=hashed_password,
        is_login=False,
        language=user.language,
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user