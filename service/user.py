from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException, status, Depends
from schema.database.user import TokenData
from sqlalchemy.orm import Session
from database.user import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from infrastructure.mysql import get_db
from schema.database.user import UserInDB,Token
from passlib.context import CryptContext
from repository.user import get_user

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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


# async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(user_name=username)
#     except jwt.PyJWTError:
#         raise credentials_exception
#
#     db_user = get_user(db, token_data.user_name)
#     if db_user is None:
#         raise credentials_exception
#     return UserInDB(
#         user_name=db_user.user_name,
#         account=db_user.account,
#         language=db_user.language,
#         is_login=db_user.is_login,
#         password=db_user.password
#     )
#
#
# async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
#     if not current_user.is_login:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user