from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException, status, Depends
from database.user import User
from infrastructure.mysql import get_db
from schema.database.notify import NotifyCreate
from schema.database.user import TokenData, UserCreate, RegisterUserRequest
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from schema.database.user import Token
from utility.auth import verify_password
import repository

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def login_for_access_token(db: Session, username: str, password: str) -> Token:
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer", is_login=True)


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


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = (TokenData(username=username))
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(db, token_data.username)
    if user is None:
        raise credentials_exception
    return user


# def validate_user_permission(db: Session, user_id: int, current_user: User):
#     db_user = db.query(User).filter(User.user_id == user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#
#     if current_user.user_name != db_user.user_name:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this user")
#
#     return db_user


def get_user(db: Session, username: str):
    return db.query(User).filter(User.user_name == username).first()


# def register_user(user: UserCreate, email: str, db: Session = Depends(get_db)):
#     print("user is here>>>>>>>>", user)
#     db_user = repository.user.create(db, user)
#
#     notify_create = NotifyCreate(type="email", data=email, user_id=db_user.id)
#     db_notify = repository.notify.create(db, notify_create)
#
#     return {"user": db_user, "notify": db_notify}


def register_user(request: RegisterUserRequest, db: Session = Depends(get_db)):
    db_user = repository.user.create(db, request.user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User creation failed")

    notify_create = NotifyCreate(type="email", data=request.email, user_id=db_user.id)
    db_notify = repository.notify.create(db, notify_create)
    if not db_notify:
        raise HTTPException(status_code=400, detail="Notification method creation failed")

    return {"user": db_user, "notify": db_notify}
